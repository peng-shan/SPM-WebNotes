from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]

class NotesUsers(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sec_password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
