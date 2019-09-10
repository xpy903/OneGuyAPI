from django.contrib import admin

from .models import AppUser
from .forms import AppUserForm

# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'create_time', 'status')
    form = AppUserForm

admin.site.register(AppUser, AppUserAdmin)
