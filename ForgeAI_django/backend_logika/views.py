from django.shortcuts import render, redirect
from ForgeAI_django import settings
from supabase import create_client, Client
from django.contrib import messages
import Korisnik;


supabase: Client = settings.supabase

def home(request):
    #user = request.session.get('user')
    ime = ""
    if supabase.auth.get_user() is not None:
        user_id = supabase.auth.get_user().user.id;
        ime = supabase.table('user_detalji').select("ime").eq("user_id", user_id).execute().data[0]['ime']
    
    #print(f"User in session: {user}")  # Debug print to ensure user is correctly fetched
    return render(request, 'home.html', {
        'ime': ime
        })

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        response = supabase.auth.sign_in_with_password({'email': email, 'password': password})
        print(f"Login response: {response}")
        if response.user:
            request.session['user'] = {
                'email': response.user.email,
                'id': response.user.id
            }
            print(f"Session user set: {request.session['user']}")
            return redirect('home')
        
            settings.korisnik = Korisnik.Korisnik(response.user.id, "prezime");
        else:
            messages.error(request, 'Invalid credentials')
        
    return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        response = supabase.auth.sign_up(
            {
                'email': email,
                'password': password
            })
        print(f"Signup response: {response}")
        
        if response.user:
            # Update the user's metadata with the name
            data, count = supabase.table('user_detalji').insert({"user_id": response.user.id, "ime": name, "prezime": "Prezime"}).execute()
            return redirect('login')
        else:
            messages.error(request, 'Sign up failed')
    
    return render(request, 'signup.html')

def logout(request):
    if 'user' in request.session:
        print("User is in session, logging out...\n")
        del request.session['user']
        supabase.auth.sign_out()  # Call Supabase sign out
    else:
        print("No user found in session.")
    return redirect('home')
