"""
MIT License

Copyright (c) 2013 Justin Bangerter
"""
from django.conf.urls import patterns, url
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from accounts.forms import ValidatingPasswordChangeForm

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'login_user', name='login'),
    url(r'^logout/$', 'logout_user', name='logout'),
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^password/change/$', password_change, {
        'template_name': 'pw_change.html',
        'post_change_redirect': reverse_lazy('accounts:pw_change_success'),
        'password_change_form': ValidatingPasswordChangeForm,
    },
        name='pw_change',
    ),
    url(r'^password/change/success/$',
        TemplateView.as_view(template_name='pw_change_success.html'),
        name='pw_change_success'
    ),
)
