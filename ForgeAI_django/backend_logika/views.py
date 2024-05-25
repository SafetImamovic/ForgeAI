from django.shortcuts import render, redirect
from supabase import create_client, Client
from ForgeAI_django import settings

supabase: Client = settings.supabase;

def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = supabase.auth.sign_up({
            'email': email,
            'password': password
            })
        # Handle user creation and redirect
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        session = supabase.auth.sign_in_with_password({
            'email': email,
            'password': password
            })
        # Handle session creation and redirect
        return redirect('home')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
