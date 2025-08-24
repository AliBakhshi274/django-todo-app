from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser, Profile

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
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
                "email", "password1", "password2", "is_staff", "is_active"
            )}
        ),
        ("permissions", {
            "fields": ("groups", "user_permissions")
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display = ('user', 'first_name', 'last_name',)
    list_filter = ('created_date',)
    readonly_fields = ('user',)
    search_fields = ('first_name', 'last_name', 'description',)
    ordering = ('user',)