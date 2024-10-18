from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):

    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        ('Logs', {'fields': ('email', 'password')}),
        ('User', {'fields': (
                    'first_name', 'last_name', 'phone'
                    )
                }
        ),
        ('Permission', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')


admin.site.register(User, UserAdmin)