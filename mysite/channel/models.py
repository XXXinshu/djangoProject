from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

