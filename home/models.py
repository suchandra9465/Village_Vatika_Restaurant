from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
def validate_contact(value):
    if  (not value.isdigit()) or not len(value)==10:
        raise ValidationError(
            _('Please enter a valid mobile number'),
            params={'value': value},
        )

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact = models.CharField(max_length=10,validators=[validate_contact])
    message = models.TextField()

    def get_absolute_url(self):
        return reverse('home:home-page')
