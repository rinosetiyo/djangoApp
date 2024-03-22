from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single_post/<int:id>', views.single_post, name='single_post'),
]