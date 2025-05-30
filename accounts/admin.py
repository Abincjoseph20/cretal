from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.


class AccountAdmin(UserAdmin):

    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    link_display_links = ('email','first_name','last_name') #when i click the email it is act like a link
    readonly_fields = ('last_login','date_joined') #date must be read only
    ordering = ('-date_joined',)

    filter_horizontal = () # we are using custom user model so we need to add this bcz display the details in admin table.
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)