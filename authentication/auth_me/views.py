#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, LoginForm

# Views for handling user interactions and rendering pages

def home(request):
    """
    Renders the home page.
    """
    return render(request, 'home.html')

def dashboard(request):
    """
    Renders the dashboard for authenticated users.
    """
    return render(request, 'dashboard.html')

def signup_view(request):
    """
    Handles user signup. Processes the signup form and creates a new user.
    If successful, redirects to the login page. Otherwise, re-displays the form with errors.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            messages.success(request, "Signup successful!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    """
    Handles user login. Authenticates user credentials and redirects to the dashboard if successful.
    Otherwise, displays an error message and reloads the login form.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('login')

def about(request):
    """
    Renders the About Us page.
    """
    return render(request, 'about.html')

def case_study(request):
    """
    Renders the Case Study page.
    """
    return render(request, 'case_study.html')

def vision(request):
    """
    Renders the Vision page.
    """
    return render(request, 'vision.html')

def contact(request):
    """
    Renders the Contact Us page.
    """
    return render(request, 'contact.html')
