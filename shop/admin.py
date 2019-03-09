from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

from shop.models import Profile, Item

admin.site.site_header = "Campiazza's Admin portal"
admin.site.site_title = "Campiazza's Admin portal"
admin.site.index_title = "All yours."


# Edit user to extend profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Remove group
admin.site.unregister(Group)


# Edit item display
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'buyer_username', 'buy_time')
    list_filter = ('buy_time','price','seller','buyer_username')
    exclude = ('buyer_id','seller','buyer_username','buy_time','buyer_address')


admin.site.register(Item,ItemAdmin)

