from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegisterForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserEditForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def user_login(request):
    form = LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            userObject = authenticate(request, username=data['username'], password=data['password'])

            if userObject is not None:
                login(request, userObject)
                return redirect('/users/')

            else:
                return render(request, 'users/login.html', {'form':form, 'invalid_credentials':True})

    return render(request, 'users/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('/users/login/')


@login_required
def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('/users/login')

    else:
        user_form = UserRegisterForm()

    return render(request, 'users/register.html', {'user_form':user_form})

@login_required
def edit(request):

    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form})