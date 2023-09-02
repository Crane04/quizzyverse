from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.info(request, "Passwords don't match!")
            return redirect("/register")
        else:
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email already exists")
                return redirect("/register")
            
            if User.objects.filter(username = username).exists():
                messages.info(request, "Email already exists")
                return redirect("/register")

            else:
                user = User.objects.create(
                    username = username, email = email, password = password1
                )

                user.save()

                return redirect("/login")
    else:
        return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        user = auth.authenticate(username= username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/new")

        else:
            messages.info(request, "Credential's don't match!")
    return render(request, "accounts/login.html")


