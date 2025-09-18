from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('recommend/', views.recommend_movie, name='recommend_movie'),
]
