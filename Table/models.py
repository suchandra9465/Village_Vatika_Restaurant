from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

def validate_date(value):
    delta = datetime.date.today()+datetime.timedelta(days=10)
    if value <= datetime.date.today():
        raise ValidationError(
            _('Date should not be less than tomorrow'),
            params={'value': value},
        )
    elif value > delta:
        raise ValidationError(
            _('Date should not be greater than 10 days from today'),
            params={'value': value},
        )


def validate_contact(value):
    if  (not value.isdigit()) or not len(value)==10:
        raise ValidationError(
            _('Please enter a valid mobile number'),
            params={'value': value},
        )

def validate_persons(value):
    if value > 4:
        raise ValidationError(
            _('%(value)s should not be greater than 4'),
            params={'value': value},
        )

def validate_time(value):
    if (value < datetime.time(11,00) or value > datetime.time(14,00)) and (value < datetime.time(18,00) or value > datetime.time(22,00)):
        raise ValidationError(
            _('Time should be either between 11 am and 2 pm or 6 pm and 10 pm'),
            params={'value': value},
        )
class BookTable(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booktables')
    customer = models.CharField(max_length=50)
    contact = models.CharField(validators=[validate_contact],max_length=10)
    email = models.EmailField(max_length=50)
    total_persons = models.IntegerField(validators=[validate_persons])
    date = models.DateField(validators=[validate_date])
    time = models.TimeField(validators=[validate_time])

    def __str__(self):
        return self.customer



    def get_absolute_url(self):
        return reverse('Table:confirm-mail')


class BookLawn(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booklawns')
    customer = models.CharField(max_length=50)
    contact = models.CharField(max_length=10,validators=[validate_contact])
    email = models.EmailField(max_length=50)
    total_persons = models.IntegerField()
    date = models.DateField(validators=[validate_date])
    time = models.TimeField()

    def __str__(self):
        return self.customer

    def get_absolute_url(self):
        return reverse('home:home-page')
