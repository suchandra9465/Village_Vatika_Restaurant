from django import forms

from .models import BookTable, BookLawn


class BookTableForm(forms.ModelForm):

    class Meta:
        model = BookTable
        fields = ('customer', 'contact','email','total_persons','date','time')
        widgets = {
            'customer':forms.TextInput(attrs={"type":"text", 'class':"form-control",'name':"name", 'placeholder':"Your Name", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Your Name'"}),
            'contact':forms.NumberInput(attrs={"type":"text", 'class':"form-control",'name':"contact", 'placeholder':"Phone Number", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Phone Number'"}),
            'email':forms.TextInput(attrs={"type":"email", 'class':"form-control",'name':"email", 'placeholder':"Email Address", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Email Address'"}),
            'total_persons':forms.NumberInput(attrs={"type":"number", 'class':"form-control",'name':"total_persons", 'placeholder':"No of Persons", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'No of Persons'"}),
            'date':forms.DateInput(attrs={"type":"text", 'class':"datepicker form-control",'name':"date", 'placeholder':"Date", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Date'"}),
            'time':forms.TimeInput(attrs={"type":"text",'id':"time",'class':"timepicker form-control",'name':"time", 'placeholder':"Time HH:MM", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Time HH:MM'"}),
        }


class BookLawnForm(forms.ModelForm):

    class Meta:
        model = BookLawn
        fields = ('customer', 'contact','email','total_persons','date','time')
        widgets = {
            'customer':forms.TextInput(attrs={"type":"text", 'class':"form-control",'name':"name", 'placeholder':"Your Name", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Your Name'"}),
            'contact':forms.NumberInput(attrs={"type":"text", 'class':"form-control",'name':"contact", 'placeholder':"Phone Number", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Phone Number'"}),
            'email':forms.TextInput(attrs={"type":"email", 'class':"form-control",'name':"email", 'placeholder':"Email Address", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Email Address'"}),
            'total_persons':forms.NumberInput(attrs={"type":"number", 'class':"form-control",'name':"total_persons", 'placeholder':"No of Persons", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'No of Persons'"}),
            'date':forms.DateInput(attrs={"type":"text", 'class':"datepicker form-control",'name':"date", 'placeholder':"Date", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Date'"}),
            'time':forms.TimeInput(attrs={"type":"text", 'class':"form-control",'name':"time", 'placeholder':"Time", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Time'"}),
        }
