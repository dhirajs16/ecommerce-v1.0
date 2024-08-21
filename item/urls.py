from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.new_item, name='new_item'),
    path('items/', views.items, name='items'),

    path('update/<int:pk>', views.update_item, name='update_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item'),
    path('detail/<int:pk>', views.detail, name='detail'), 
]