from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'users': Profile.objects
        if request.user.is_authenticated else []
    }

    return render(request, 'googleauth/index.html', context)


def users_list(request):
    users_list = Profile.objects.order_by('-user')
    context = {
        'users_list': users_list,
    }
    return render(request, 'googleauth/list.html', context)


@login_required(login_url='/')
def update_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            user_form = UserForm()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'googleauth/edit.html', {'user_form': user_form, 'profile_form': profile_form})
