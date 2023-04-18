from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _


class User(AbstractUser):
	username = models.CharField(
    max_length=50, blank=True, null=True, unique=False, default="")
	email = models.EmailField(_('email address'), unique=True)
	phone_number = models.CharField(max_length=15, null=True, blank=True)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

	def __str__(self):
		return str(self.email)
