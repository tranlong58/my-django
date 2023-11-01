from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import bcrypt

from ..models.Admins import Admins

# Create your views here.

def index(request):
    admin_list = Admins.objects.all().order_by("id")
    user_name = request.session.get('user_name', '')
    context = {
        'admin_list': admin_list,
        'user_name': user_name,
    }
    return render(request, 'admin_page/admin.html', context)


@csrf_exempt
def create(request):
    name = request.POST['add-name']
    email = request.POST['add-email']
    password = request.POST['add-password']
    salt = bcrypt.gensalt()
    hashPassword = bcrypt.hashpw(password.encode('utf-8'), salt)

    new_admin = Admins(
        name = name, 
        email = email, 
        password = hashPassword,
    )
    new_admin.save()
    return redirect('admin_page:admin-index')


@csrf_exempt
def update(request):
    admin_id = request.POST['edit-id']
    updated_admin = Admins.objects.get(pk=admin_id)

    password = request.POST['edit-password']
    salt = bcrypt.gensalt()
    hashPassword = bcrypt.hashpw(password.encode('utf-8'), salt)

    updated_admin.name = request.POST['edit-name']
    updated_admin.email = request.POST['edit-email']
    updated_admin.password = hashPassword

    updated_admin.save()
    return redirect('admin_page:admin-index')


@csrf_exempt
def delete(request):
    admin_id = request.POST['delete-id']
    deleted_admin = Admins.objects.get(pk=admin_id)

    deleted_admin.delete()
    return redirect('admin_page:admin-index') 