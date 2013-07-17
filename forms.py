"""
MIT License

Copyright (c) 2013 Justin Bangerter
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )


class ValidatingPasswordChangeForm(PasswordChangeForm):
    MIN_LENGTH = 8

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            pattern = "The new password must be at " \
                      "least %d characters long."
            raise forms.ValidationError(pattern % self.MIN_LENGTH)

        # the super class operates on password2
        return password1
