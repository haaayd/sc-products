from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='profiles_detail')

]