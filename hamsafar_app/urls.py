from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('hamsafars/', views.hamsafar_list, name='hamsafar_list'),
    path('hamsafars/create/', views.create_hamsafar, name='create_hamsafar'),
]