from django.contrib import admin
from .models import Category, Item

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description','image', 'price', 'is_sold', 'created_by', 'created_at']