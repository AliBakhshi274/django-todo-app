from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_active',)
    fieldsets = (
        ('Authentication', {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff","is_active"
            )}
        ),
        ('Permissions',{
            'fileds': (
                "groups", "user_permissions"
            )
        })
    )
    search_fields = ("email",)
    ordering = ("email",)