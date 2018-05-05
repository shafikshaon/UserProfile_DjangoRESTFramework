from django.contrib import admin
from .models import Profile, UserFeedItem


# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'user_name', 'email')


    def full_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    def user_name(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


class UserFeedItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'status_text', 'created_at')

    def full_name(self, obj):
        return obj.user_profile.user.first_name + " " + obj.user_profile.user.last_name

    def username(self, obj):
        return obj.user_profile.user.username


admin.site.register(Profile, UserProfileAdmin)
admin.site.register(UserFeedItem, UserFeedItemAdmin)