from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # define signals so our Profile model will be automatically
    # created/updated when we create/update User instances
    # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class UserFeedItem(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
