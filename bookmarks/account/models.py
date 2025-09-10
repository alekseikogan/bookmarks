from django.db import models
from django.conf import settings


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

    objects = models.Manager()
    active = ProfileManager()  # Profile.active.all() returns only active users

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
