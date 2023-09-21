from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'date_joined')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        # (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('date_joined', 'last_login',)}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )

    # add_fieldsets = (
    #     (None, {
    #         # 'classes': ('wide',),
    #         'fields': ('email', 'username', 'password'),
    #     }),
    # )

admin.site.register(Account, AccountAdmin)
