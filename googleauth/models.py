from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<username>.extention(.jpg/.png)
    extention = filename.split('.')
    return '{0}/{1}.{2}'.format(instance.user.username, instance.user.username, extention[1])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    pic = models.ImageField(upload_to=user_directory_path, blank=True, default='/default.png')

    def __str__(self):
        return '%s' % (self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
