from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views


# Create your views here.
def register (request):
    """show the registration form"""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                    )
                user.save()
                # display a message
                messages.success(request, "Account created successfully")
                return redirect('accounts:login')
            except:
                # display a message if the above fails
                messages.error(request, "Username already exists")
        else:
            # display amessage saying passwords do not match
            messages.error(request, "Passwords do not match")

    return render(request,'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('final_app:home')   
        else:
            messages.error(request, "Wrong Password")
    return render(request,'accounts/login.html')

def logout_view(request):
    return auth_views.LogoutView.as_view()(request)

def logout_view(request):
    """Handles logging out the user"""
    logout(request)  # Logs out the user
    messages.success(request, "Logout Successful!")  # Show success message
    return redirect('final_app:home')  # Redirect to the home page or any other page