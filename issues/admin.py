from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Type)
