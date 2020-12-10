from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, BlogComment
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    ordering = ['-blog_date']


class BlogsView(DetailView):
    model = BlogPost
    template_name = 'Blogs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogsView, self).get_context_data(*args, **kwargs)
        get_likes = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        total_likes = get_likes.total_likes()
        liked = False
        if get_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


# def blog_category_list_view(request):
#     cat_menu_list = Category.objects.all()
#     return render(request, 'Blog_Categories_List.html', {'cat_menu_list': cat_menu_list})


# def blog_category_view(request, cats):
#     category_posts = BlogPost.objects.filter(category=cats)
#     return render(request, 'Blog_Categories.html', {'cats': cats.title(), 'category_posts': category_posts})


def likeview(request, pk):
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    liked = False
    if blogpost.likes.filter(id=request.user.id).exists():
        blogpost.likes.remove(request.user)
        liked = False
    else:
        blogpost.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blogs', args=[str(pk)]))


class AddBlogView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'Add_Blog.html'


# class AddBlogCategoryView(CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'Add_Blog_Category.html'


class UpdateBlogView(UpdateView):
    model = BlogPost
    template_name = 'Update_Blog.html'
    form_class = UpdateForm


class DeleteBlogView(DeleteView):
    model = BlogPost
    template_name = 'Delete_Blog.html'
    success_url = reverse_lazy('home')


# class BlogCommentView(CreateView):
#     model = BlogComment
#     template_name = 'Add_Comment.html'
#     form_class = CommentForm
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         form.instance.blog_id = self.kwargs['pk']
#         return super().form_valid(form)
