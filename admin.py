"""
MIT License

Copyright (c) 2013 Justin Bangerter
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import UserProfile

class UserProfileInline(admin.StackedInline):
  """
  A new inline admin descriptor for the custom user profile
  """
  model = UserProfile
  can_delete = False
  verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
  """
  A new user admin
  """
  inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
