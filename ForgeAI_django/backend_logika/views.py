from django.shortcuts import render, redirect
from ForgeAI_django import settings
from supabase import create_client, Client
from django.contrib import messages

supabase: Client = settings.supabase

def home(request):
    user = request.session.get('user')
    ime = ""
    if user:
        user_id = user['id']
        user_details = supabase.table('user_detalji').select("ime").eq("user_id", user_id).execute().data
        if user_details:
            ime = user_details[0]['ime']
    
    return render(request, 'home.html', {
        'ime': ime
    })

def login(request):
    user = request.session.get('user')
    if user:
        return redirect('home')
        
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        response = supabase.auth.sign_in_with_password({'email': email, 'password': password})
        if response.user:
            request.session['user'] = {
                'email': response.user.email,
                'id': response.user.id
            }
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
        
    return render(request, 'login.html')

def signup(request):
    user = request.session.get('user')
    if user:
        return redirect('home')
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        response = supabase.auth.sign_up({'email': email, 'password': password})
        if response.user:
            # Update the user's metadata with the name
            supabase.table('user_detalji').insert({"user_id": response.user.id, "ime": name, "prezime": "Prezime"}).execute()
            return redirect('login')
        else:
            messages.error(request, 'Sign up failed')
    
    return render(request, 'signup.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        supabase.auth.sign_out()
    return redirect('home')
