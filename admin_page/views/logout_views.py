from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here.

@csrf_exempt
def logout(request):
    token = request.session.get('token', '')
    user_name = request.session.get('user_name', '')
    if token:
        request.session.pop('token')
    if user_name:
        request.session.pop('user_name')
    return redirect('login_page:login') 