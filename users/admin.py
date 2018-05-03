from django.contrib import admin
from .models import Profile


# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'user_name', 'email')


    def full_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def user_name(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


admin.site.register(Profile, UserProfileAdmin)