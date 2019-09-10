from django.contrib import admin

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'picture_url', 'grade','parent_id')
    fields = ('name', 'code', 'picture_url', 'parent', 'grade')
    search_fields = ('code', 'name')
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)