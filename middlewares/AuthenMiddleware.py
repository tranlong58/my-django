from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

from admin_page.models.Admins import Admins

class AuthenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ('/login/', '/authen/') :
            return self.get_response(request) 

        try: 
            token = request.session.get('token', '')
            if token == '':
                raise TokenError('Token is empty')
            
            token_obj = AccessToken(token)
            payload = token_obj.payload
            email = payload.get('email') 
            
            # verify email
            admin = Admins.objects.get(email=email)

        except (TokenError, Admins.DoesNotExist):
            request.session['err'] = 'You have to sign in'  
            return redirect('login_page:login')

        return self.get_response(request)
