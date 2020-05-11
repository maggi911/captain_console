from django.shortcuts import render, redirect, get_object_or_404
#from user.models import ProfileImage
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from user.forms.profile_form import ProfileForm
from user.forms.register import RegisterForm, EditProfileForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_image = ProfileForm(profile_image=request.POST["profile_image"], user=user)
            profile_image.save()
            return redirect("login")
    return render(request, "user/register.html", {
        "form": RegisterForm()
    })

def get_user_by_id(request):
    return render(request, "user/profile.html", {
        "user": get_object_or_404(User, pk=request.user.id)
    })

def edit_profile(request):
    instance = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=instance)
    return render(request, "user/edit_profile.html", {
        "form": form,
        "id": request.user.id
    })

