from django.db import models
from django.utils import timezone
from authentication.models import User
# Create your models here.


class Type(models.Model):
    description = models.CharField(max_length=128)


class Issue(models.Model):
    STATUS = (
        ('todo', 'todo'),
        ('in progress', 'in progress'),
        ('done', 'done')
    )

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1500)
    current_status = models.CharField(
        max_length=20, choices=STATUS, default='todo')
    vote_amount = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    issue = models.ForeignKey(Issue, on_delete=models.PROTECT)
    description = models.CharField(max_length=1500)
    vote_amount = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.description
