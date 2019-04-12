from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,CreateView)
from . models import Menu
from . forms import MenuForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class MenuListView(ListView):
    model = Menu
    context_object_name = 'menu_list'

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('home:home-page')
    else:
        form = MenuForm()

    return render(request,'menu/menu_form.html',{'form':form})
