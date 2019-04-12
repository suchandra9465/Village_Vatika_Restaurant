from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('rating', 'drop_a_note', 'suggest_menu_item')
        # widgets = {
        #     'rating': forms.NumberInput(attrs={'class':'StarRating'}),
        #         }
