from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),    
    path('contacts/', views.contacts, name='contacts'),    
    path('signup/', views.signup, name='signup'),    
    path('login/', views.log_in, name='login'),    
    path('logout/', views.log_out, name='logout'),    
    path('dashboard/', views.dashboard, name='dashboard'),    
]