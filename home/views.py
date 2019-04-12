from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Contact
from .forms import ContactForm
# Create your views here.
app_name = 'home'
class GalleryPage(TemplateView):
    template_name = 'home/gallery.html'

class HomePage(TemplateView):
    template_name = 'home/index.html'

class CreateContact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'

@login_required
@user_passes_test(lambda u: u.is_superuser)
def contact_mess_listview(request):
    query1 = Contact.objects.all()
    return render(request,'home/contact_message.html',{'query1':query1})