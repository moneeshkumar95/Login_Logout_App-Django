from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('home/log_out/', views.log_out, name='log_out'),
    path('log_out/', views.log_out, name='log_out'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name= 'password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_sent.html') , name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html') , name= 'password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html') , name= 'password_reset_complete'),
]