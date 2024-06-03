from django.shortcuts import render, redirect
from payments.models import CheckoutSessionRecord
from django.http import JsonResponse
import openai
from .models import Chat
from django.utils import timezone
import google.generativeai as genai
import os



genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel(model_name='gemini-1.5-flash')


def ask_gemani(message):
    response = model.generate_content(message)
    
    return response.text


def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    try:
        record = CheckoutSessionRecord.objects.get(user=request.user)
    except CheckoutSessionRecord.DoesNotExist:
        return redirect('subscribe')
    
    chats = Chat.objects.filter(user=request.user).order_by('created_at')

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemani(message)
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    context = {'chats': chats, 'record': record}
    return render(request, 'sessions.html', context)
