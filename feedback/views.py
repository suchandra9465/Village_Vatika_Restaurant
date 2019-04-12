from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.

class CreateFeedback(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    def form_valid(self, form):
        feedback = form.save(commit=False)
        form.instance.review_by = self.request.user
        return super(CreateFeedback,self).form_valid(form)

class DisplayRatings(ListView):
    model = Feedback
    context_object_name = 'ratings'
    template_name = 'home/index.html'
