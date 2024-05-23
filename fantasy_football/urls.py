from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from leagues import views as league_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', league_views.register, name='register'),
    path('', league_views.home, name='home'),
    path('league/<int:league_id>/', league_views.league_detail, name='league_detail'),
    path('team/<int:team_id>/', league_views.team_detail, name='team_detail'),
    path('upload/', league_views.upload_file, name='upload_file'),
    path('leagues/', league_views.all_leagues, name='all_leagues'),
    path('teams/', league_views.all_teams, name='all_teams'),
    path('my_team/', league_views.my_team, name='my_team'),
    path('assign_players/', league_views.assign_players, name='assign_players'),
]
