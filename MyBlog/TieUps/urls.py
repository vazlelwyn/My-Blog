from django.urls import path
from .views import TieupView, TieUpDetailView, AddTieUpView, UpdateTieUpView, DeleteTieUpView


urlpatterns = [
    path('', TieupView.as_view(), name='tie_up_list'),
    path('<int:pk>/', TieUpDetailView.as_view(), name='tie_up_details'),
    path('Add_TieUp/', AddTieUpView.as_view(), name='add_tie_up'),
    path('Edit/<int:pk>/', UpdateTieUpView.as_view(), name='update_tie_up'),
    path('<int:pk>/Delete', DeleteTieUpView.as_view(), name='delete_tie_up'),
]