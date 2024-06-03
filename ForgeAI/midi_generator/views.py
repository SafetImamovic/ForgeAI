from django.shortcuts import render, redirect
from payments.models import CheckoutSessionRecord
from django.http import JsonResponse
import openai
from .models import Chat
from django.utils import timezone

openai_api_key = 'sk-proj-uusy9oKkBTUvfQKKJ91iT3BlbkFJYTSc8n6ZYhSlojwPmTei'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    answer = response.choices[0].text.strip()
    return answer


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
        response = "test response"
        
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    context = {'chats': chats, 'record': record}
    return render(request, 'sessions.html', context)
