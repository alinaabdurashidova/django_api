from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_gadgets),
    path("create/", create_gadget),
    path('get/<int:pk>/', get_one_gadget),
    path('update/<int:pk>/', update_gadget),
    path('delete/<int:pk>/', delete_gadget),
    path('<int:pk>/', detail)
]