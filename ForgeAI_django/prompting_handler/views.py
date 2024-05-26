from django.shortcuts import render;
from supabase import create_client, Client
from ForgeAI_django import settings

supabase: Client = settings.supabase

def prompts(request):
    context = {
        'info': ''
    }
    
    if supabase.auth.get_user() is not None:
        context = {
        'info': ''
    }
    else:
        context = {
                'info': 'Korisnik nije ulogovan!'
            }
    
    if request.method == 'POST':
        prompt = request.POST['prompt'];
        
        if supabase.auth.get_user() is not None:
            user_id = supabase.auth.get_user().user.id;
            response = supabase.table('prompts').insert({'prompt': prompt, 'user_id': user_id}).execute();
            
    return render(request, 'prompts.html', context);