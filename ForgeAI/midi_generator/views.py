from django.shortcuts import render, redirect

def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    return render(request, 'sessions.html')
