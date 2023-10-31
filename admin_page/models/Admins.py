from django.db import models

# Create your models here.

class Admins(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'admins'