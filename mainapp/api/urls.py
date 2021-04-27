from django.urls import path

from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('category', views.BlogCategoryViewSet, basename='category')
router.register('blogpost', views.BlogPostViewSet, basename='blogpost')

urlpatterns = []

urlpatterns += router.urls
