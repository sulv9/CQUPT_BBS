from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account
from .models import Topic, Article

class AccountInline(admin.StackedInline):
    model =Account
    can_delete = False
    verbose_name_plural = 'Account'

class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)


# Register your models here.
admin.site.register(Account)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Topic)
admin.site.register(Article)
