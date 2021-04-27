from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('category/<int:id>/', views.category_detail),
    path('post/<int:id>', views.post_detail),
]
