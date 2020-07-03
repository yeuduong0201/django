from .models import Question, Choice
from django import forms 

class formQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class formChoice(forms.ModelForm):
    class Meta:
        model = Choice 
        fields = '__all__'