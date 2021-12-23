from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('username', 'first_name',
            'last_name', 'middle_name', 'department', 'duty', 'age',
            'salary', 'photo', 'is_active', 'is_superuser')}),
        ('Password info', {'fields': ('password',)}),
        ('Groups, permissions', {
            'fields': ('groups', 'user_permissions'),
        })
        )

    add_fieldsets = (
        ('Create', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'middle_name', 'password1', 'password2', 'department', 'duty', 'age', 'salary', 'photo'),
        }),
        )

    list_display = ('username', 'first_name', 'last_name', 'middle_name', 'department', 'is_active')
    search_fields = ('first_name', 'last_name', 'middle_name', 'department')
    ordering = ('first_name', 'last_name','middle_name')