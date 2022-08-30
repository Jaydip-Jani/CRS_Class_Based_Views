from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'is_admin']
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('id', 'email', 'username', 'password',), }),
    )
    search_fields = ('username',)
    ordering = ('id', 'username',)
    filter_horizontal = ()


admin.site.register(Customer, UserModelAdmin),
admin.site.register(Car)
admin.site.register(Reservation)


