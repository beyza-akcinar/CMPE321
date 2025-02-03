from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('audience-login/', views.audience_login, name='audience_login'),
    path('director-login/', views.director_login, name='director_login'),
    path('manager-login/', views.manager_login, name='manager_login'),
    path('audience-home/', views.audience_home, name='audience_home'),
    path('director-home/', views.director_home, name='director_home'),
    path('manager-home/', views.manager_home, name='manager_home'),
    path('delete-audience/', views.delete_audience, name='delete_audience'),
    path('delete-director/', views.delete_director, name='delete_director'),     
    path('add-director/', views.add_director, name='add_director'),  
    path('add-audience/', views.add_audience, name='add_audience'),     
    path('update-platform/', views.update_platform, name='update_platform'), 
    path('add-movie/', views.add_movie, name='add_movie'),
    path('add-predecessor/', views.add_predecessor, name='add_predecessor'),  
    path('update-name/', views.update_name, name='update_name'),  
    path('view-directors/', views.view_directors, name='view_directors'),  
    path('view-ratings/', views.view_ratings, name='view_ratings'),  
    path('view-movies/', views.view_movies, name='view_movies'),  
    path('view-average-rating/', views.view_average_rating, name='view_average_rating'),  
    path('view-directed-movies/', views.view_directed_movies, name='view_directed_movies'),  
    path('view-all-movies/', views.view_all_movies, name='view_all_movies'),
    path('buy-ticket/', views.buy_ticket, name='buy_ticket'),   
    path('bought-tickets/', views.bought_tickets, name='bought_tickets'),   
    path('view-audience/', views.view_audience, name='view_audience'),   
                     
]