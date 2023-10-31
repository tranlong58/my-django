from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views import generic

from ..models.Admins import Admins

# Create your views here.

class IndexView(generic.ListView):
    template_name = "admin_page/admin.html"
    context_object_name = "admin_list"

    def get_queryset(self):
        return Admins.objects.all().order_by("id")


@csrf_exempt
def create(request):
    new_admin = Admins(
        name = request.POST['add-name'],
        email = request.POST['add-email'],
        password = request.POST['add-password'],
    )
    new_admin.save()
    return redirect('admin_page:admin-index')


@csrf_exempt
def update(request):
    admin_id = request.POST['edit-id']
    updated_admin = Admins.objects.get(pk=admin_id)

    updated_admin.name = request.POST['edit-name']
    updated_admin.email = request.POST['edit-email']
    updated_admin.password = request.POST['edit-password']

    updated_admin.save()
    return redirect('admin_page:admin-index')


@csrf_exempt
def delete(request):
    admin_id = request.POST['delete-id']
    deleted_admin = Admins.objects.get(pk=admin_id)

    deleted_admin.delete()
    return redirect('admin_page:admin-index') 