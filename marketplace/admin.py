from django.contrib import admin
from .models import ReviewRating

from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'packageitem', 'quantity', 'updated_at')

from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'packageitem', 'quantity', 'updated_at')

# Register your models here.
