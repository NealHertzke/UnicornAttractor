from django.db import models
from django.contrib.auth.models import User as AuthUser
# Create your models here.


class User(AuthUser):
    class Meta:
        proxy = True
