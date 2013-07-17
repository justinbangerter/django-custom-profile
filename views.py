"""
MIT License

Copyright (c) 2013 Justin Bangerter
"""
from django.core.context_processors import csrf
from django.shortcuts import\
    render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import\
    authenticate, login, logout
from accounts.forms import\
    UserForm, UserProfileForm
from django.core.urlresolvers import reverse
from accounts.models import User
from django.contrib.auth.decorators import\
    login_required


def login_user(request, template='login.html'):
    """
    Handle the log in process
    """
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('accounts:profile'))
            else:
                state = "Your account is not active, " \
                        "please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    d = {'state': state, 'username': username}
    d.update(csrf(request))
    return render_to_response(template, d, RequestContext(request))


def logout_user(request):
    """
    Log a user out of the system
    """
    logout(request)
    return redirect('/')


@login_required
def profile(request, template='profile.html'):

    user = User.objects.get(id=request.user.id)
    profile = user.get_profile()

    uform = UserForm(instance=user)
    pform = UserProfileForm(instance=profile)

    if request.method == "POST":
        uform = UserForm(data=request.POST, instance=user)
        pform = UserProfileForm(data=request.POST, instance=profile)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()

    return render_to_response(template, {
        'user_form': uform,
        'profile_form': pform,
    }, RequestContext(request))
