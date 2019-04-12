from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateFeedback.as_view(),name = 'feedback'),
]
