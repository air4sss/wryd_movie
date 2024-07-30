# movies/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.search_movie, name='search_movie'),
    path('search_form/', views.search_form, name='search_form'),
    path('reviews/<int:id>/', views.movie_reviews, name='movie_reviews'),
    path('info/<int:id>/', views.get_movie_info, name='get_movie_info'),
    path('set_language/', views.set_language, name='set_language'),
    path('send-message/', views.send_message, name='send_message'),

]
