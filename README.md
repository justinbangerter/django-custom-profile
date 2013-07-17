django-custom-profile
=====================

This is a template to help you get started with custom user profiles.  

I got tired of digging through projects and moving this code around.

Just clone this into a subfolder of your repository and add the following line to your `settings.py`

    AUTH_PROFILE_MODULE = 'accounts.UserProfile'

Also, add `'accounts',` as a line in your `INSTALLED_APPS` setting in `settings.py`

---

There are some tests, but I removed my fixtures to protect the innocent.  Go ahead and tweak the tests and the templates.
