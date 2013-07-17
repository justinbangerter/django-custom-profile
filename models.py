"""
MIT License

Copyright (c) 2013 Justin Bangerter
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    Additional information about a user
    """
    user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
        return unicode(self.user)


def create_user_profile(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
