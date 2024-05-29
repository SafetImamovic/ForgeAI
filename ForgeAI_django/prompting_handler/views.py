from supabase import Client
import supabase
from ForgeAI_django import settings
from django.shortcuts import render, redirect
from .forms import ChatForm
from django.contrib import messages
from .data_klase import ChatSesija, Poruka
from stripe_pretplata import models

supabase: Client = settings.supabase

def index(request):
    user = request.session.get('user')
    if not user:
        messages.error(request, 'You need to be logged in to access chat sessions.')
        return redirect('login')
    
    response_s = supabase.table('stripe_pretplata_checkoutsesijazapis').select('*').eq('user_uuid', user['id']).execute();
    
    if (len(response_s.data) == 0):
        return redirect('pretplati')
    
    checkout_record = models.CheckoutSesijaZapis.objects.get(
        user_uuid=user['id']
    )
    
    if (checkout_record.ima_pristup == False):
        return redirect('pretplati')
        
    response = supabase.table('chat_sesije').select('*').eq('user_id', user['id']).execute()
    chat_sessions_data = response.data
    
    chat_sessions = []
    for session_data in chat_sessions_data:
        chat_sessions.append(ChatSesija(
            id=session_data['id'],
            session_name=session_data['sesija_ime'],
            messages=[],
            created_at=session_data['created_at']
        ))

    return render(request, 'chatbot/index.html', {'chat_sessions': chat_sessions})

def chat_session(request, session_id):
    user = request.session.get('user')
    if not user:
        messages.error(request, 'You need to be logged in to access this chat session.')
        return redirect('login')
    
    response_s = supabase.table('stripe_pretplata_checkoutsesijazapis').select('*').eq('user_uuid', user['id']).execute();
    
    if (len(response_s.data) == 0):
        return redirect('pretplati')
    
    checkout_record = models.CheckoutSesijaZapis.objects.get(
        user_uuid=user['id']
    )
    
    if (checkout_record.ima_pristup == False):
        return redirect('pretplati')
    
    session_response = supabase.table('chat_sesije').select('*').eq('id', session_id).eq('user_id', user['id']).execute()
    
    if not session_response.data:
        messages.error(request, 'Chat session not found or you do not have permission to access it.')
        return redirect('index')
    
    session_data = session_response.data[0]
    chat_session = ChatSesija(
        id=session_data['id'],
        session_name=session_data['sesija_ime'],
        messages=[],
        created_at=session_data['created_at']
    )
    
    messages_response = supabase.table('poruke').select('*').eq('chat_sesija_id', session_id).order('created_at', desc=False).execute()
    messages_data = messages_response.data
    jeKorisnik = supabase.table('poruke').select('je_korisnik').eq('chat_sesija_id', session_id).execute()

    for message_data in messages_data:
        chat_session.messages.append(Poruka(
            message_text=message_data['poruka_text'],
            is_user=message_data['je_korisnik'],
            timestamp=message_data['created_at']
        ))
    
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            supabase.table('poruke').insert({'chat_sesija_id': session_id, 'poruka_text': user_input, 'je_korisnik': True}).execute()
            # Add logic to get the bot's response
            bot_response = "This is a bot response."
            supabase.table('poruke').insert({'chat_sesija_id': session_id, 'poruka_text': bot_response, 'je_korisnik': False}).execute()
            return redirect('chat_session', session_id=session_id)
    else:
        form = ChatForm()

    return render(request, 'chatbot/chat_session.html', {'chat_session': chat_session, 'messages': messages, 'je_korisnik': jeKorisnik, 'form': form})

def create_session(request):
    user = request.session.get('user')
    if not user:
        messages.error(request, 'You need to be logged in to create a chat session.')
        return redirect('login')
    
    response_s = supabase.table('stripe_pretplata_checkoutsesijazapis').select('*').eq('user_uuid', user['id']).execute();
    
    if (len(response_s.data) == 0):
        return redirect('pretplati')
    
    checkout_record = models.CheckoutSesijaZapis.objects.get(
        user_uuid=user['id']
    )
    
    if (checkout_record.ima_pristup == False):
        return redirect('pretplati')
    
    if request.method == "POST":
        session_name = request.POST['session_name']
        response = supabase.table('chat_sesije').insert({'sesija_ime': session_name, 'user_id': user['id']}).execute()
        session_id = response.data[0]['id']
        return redirect('chat_session', session_id=session_id)
    return render(request, 'chatbot/create_session.html')
