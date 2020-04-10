from django.contrib import admin
from .models import MyURL
# Register your models here.
@admin.register(MyURL)
class MyURLAdmin(admin.ModelAdmin):
    pass
 
