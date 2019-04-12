from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','contact','message')
        widgets = {
            'name':forms.TextInput(attrs={"type":"text", 'class':"common-input mb-20 form-control",'name':"name", 'placeholder':"Enter your name", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Your Name'"}),
            'contact':forms.NumberInput(attrs={"type":"text", 'class':"common-input mb-20 form-control",'name':"contact", 'placeholder':"Phone number", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Phone Number'"}),
            'email':forms.TextInput(attrs={"type":"email", 'class':"common-input mb-20 form-control",'name':"email", 'placeholder':"Email address", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Email Address'"}),
            'message':forms.Textarea(attrs={"type":"text", 'class':"common-textarea form-control",'name':"message", 'placeholder':"Message", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Message'"}),
            }
