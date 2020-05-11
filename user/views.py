from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from user.forms.register import RegisterForm, EditProfileForm
from user.models import Profile


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_image = Profile(profile_image=request.POST["profile_image"], user=user)
            profile_image.save()
            return redirect("login")
        else:
            print(form.errors)
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
            profile = get_object_or_404(Profile, user=instance)
            profile.delete()
            profile_image = Profile(profile_image=request.POST["profile_image"], user=instance)
            profile_image.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=instance)
    return render(request, "user/edit_profile.html", {
        "form": form,
        "id": request.user.id
    })

