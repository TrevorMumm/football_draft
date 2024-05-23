from django.contrib import admin
from django.urls import path, include
from leagues import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('create_league/', views.create_league, name='create_league'),
    path('league/<int:league_id>/', views.league_detail, name='league_detail'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('upload/', views.upload_file, name='upload_file'),
    path('leagues/', views.all_leagues, name='all_leagues'),
    path('teams/', views.all_teams, name='all_teams'),
]
