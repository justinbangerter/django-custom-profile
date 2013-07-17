django-custom-profile
=====================

This is a template to help you get started with custom user profiles.  

I got tired of digging through projects and moving this code around, so here it is.

---

First, clone this repository into a subfolder of your repository 
and add the following line to your `settings.py` (just copy the folder, don't bother
making a submodule)

    AUTH_PROFILE_MODULE = 'accounts.UserProfile'

Finally, add `'accounts',` as a line in your `INSTALLED_APPS` setting in `settings.py`

---

There are some tests, but I removed my fixtures to protect the innocent.  
You will have to tweak the tests and the templates for your own purposes if you would like
to use them.
