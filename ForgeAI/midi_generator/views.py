from django.shortcuts import render, redirect
from payments import models
from payments.models import CheckoutSessionRecord
from django.http import JsonResponse
import openai



openai_api_key = 'sk-proj-uusy9oKkBTUvfQKKJ91iT3BlbkFJYTSc8n6ZYhSlojwPmTei'
openai.api_key = openai_api_key

def ask_openai(message):

    response = openai.Completion.create (
        model="text-davinci-003",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    answer = response.choice[0].text.strip()
    return answer

def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    try:
        record = CheckoutSessionRecord.objects.get(user=request.user)
    except CheckoutSessionRecord.DoesNotExist:
        return redirect('subscribe')
    
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        
        chat = Chat(user=request.user, message=message, response=response)

        return JsonResponse({'message': message, 'response': response})

    return render(request, 'sessions.html', context={'record': record})
