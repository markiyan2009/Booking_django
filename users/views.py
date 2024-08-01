from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.forms import CustomUserCreationForm



# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
        messages.error(request,message="some error")
    return render(request,template_name="users/register.html",context={"form":form})

def login(request):
    if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect("home")
                else:
                    messages.error(request,message="Wrong username or password")

    else:
        return render(request,template_name="users/login.html")
    