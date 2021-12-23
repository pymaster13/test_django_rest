from django.contrib import admin

from .models import Department

admin.site.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'count_persons', 'count_salary')
    search_fields = ('name', 'director')
    ordering = ('name',)


    
