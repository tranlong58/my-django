from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from rest_framework_simplejwt.tokens import AccessToken

from admin_page.models.Admins import Admins

# Create your views here.

def login(request):
    err = request.session.get('err', '')
    if err:
        request.session.pop('err')
    return render(request, 'login_page/login.html', {'err': err})


@csrf_exempt
def authen(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        admin = Admins.objects.get(email=email)
        storedPassword = admin.password[2:-1].encode('utf-8')

        if bcrypt.checkpw(password.encode('utf-8'), storedPassword):
            token = AccessToken()
            token.payload.update({'email': email})
            request.session['token'] = str(token)
            request.session['user_name'] = admin.name 
            return redirect('admin_page:admin-index')
        else:
            request.session['err'] = 'Wrong password'  
            return redirect('login_page:login')
    except Admins.DoesNotExist:
        request.session['err'] = 'Wrong email'  
        return redirect('login_page:login')