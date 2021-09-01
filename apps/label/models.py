from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from apps.book.models import Book
from apps.university.models import University
from apps.user.models import Profile


class Label(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    inventory = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=8)
    tag_id = models.CharField(max_length=64, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)


class UserLabel(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    inventory = models.CharField(max_length=30, null=True, blank=True)
    tag_id = models.CharField(max_length=64, null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)