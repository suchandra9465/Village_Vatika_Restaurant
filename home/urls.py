from django.urls import path
from . import views
from feedback import views as feedviews


urlpatterns = [
    path('',feedviews.DisplayRatings.as_view(),name='home-page'),
    path('gallery/',views.GalleryPage.as_view(), name = "gallery-page"),
    path('contact/',views.CreateContact.as_view(),name='contact'),
    path('contact_messages/',views.contact_mess_listview, name = 'contact_list'),
]
