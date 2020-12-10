from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostImage
from .forms import AddTieUpForm, AddTieUpImagesForm, UpdateTieUpForm
from django.forms import inlineformset_factory
from django.urls import reverse_lazy


# Create your views here.


class TieupView(ListView):
    model = Post
    template_name = 'Tie_up.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TieupView, self).get_context_data(*args, **kwargs)
        return context


class TieUpDetailView(DetailView):
    model = Post
    template_name = 'Tie_Up_Details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TieUpDetailView, self).get_context_data(*args, **kwargs)
        photos = PostImage.objects.filter(post=self.kwargs['pk'])
        context['photos'] = photos
        return context


AddTieUpImagesFormSet = inlineformset_factory(Post, PostImage, form=AddTieUpImagesForm, fields=['images'], extra=3, can_delete=True)


class AddTieUpView(CreateView):
    model = Post
    form_class = AddTieUpForm
    template_name = 'Add_Tie_Up.html'
    success_url = reverse_lazy('tie_up_list')

    def get_context_data(self, **kwargs):
        data = super(AddTieUpView, self).get_context_data(**kwargs)
        data['images'] = AddTieUpImagesFormSet()
        if self.request.POST:
            data['images'] = AddTieUpImagesFormSet(self.request.POST, self.request.FILES)
        else:
            data['images'] = AddTieUpImagesFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        with transaction.atomic():
            form.instance.author.id = self.request.user.id
            self.object = form.save()
            if images.is_valid():
                images.instance = self.object
                images.save()
        return super(AddTieUpView, self).form_valid(form)


class UpdateTieUpView(UpdateView):
    model = Post
    form_class = UpdateTieUpForm
    template_name = 'Update_Tie_Up.html'
    success_url = reverse_lazy('tie_up_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['images'] = AddTieUpImagesFormSet()
        if self.request.POST:
            data['images'] = AddTieUpImagesFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['images'] = AddTieUpImagesFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        self.object = form.save()
        if images.is_valid():
            images.instance = self.object
            images.save()
        return super(UpdateTieUpView, self).form_valid(form)


class DeleteTieUpView(DeleteView):
    model = Post
    template_name = 'Delete_Tie_Up.html'
    success_url = reverse_lazy('tie_up_list')