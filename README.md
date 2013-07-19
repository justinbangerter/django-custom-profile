django-custom-profile
=====================

This is a template to help you get started with custom user profiles.  

I got tired of digging through projects and moving this code around, so here it is.

---

First, clone this repository into a subfolder of your repository
(just copy the folder, don't bother making a submodule).

Then, add the following line to your `settings.py`

    AUTH_PROFILE_MODULE = 'accounts.UserProfile'

Finally, add `'accounts',` as a line in your `INSTALLED_APPS` setting in `settings.py`

---

You will have to tweak the tests and the templates for your own purposes if you would like
to use them.

Also, I have only ever used this code in hobby projects, so make sure that users can't alter each
other's profiles or engage in any other nonsense.

In other words, take the time to test this yourself before using it in a production setting.

If you find something wrong or missing, please submit an issue and/or a pull request.

HTH
