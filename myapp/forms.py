from django import forms
from django.forms import ModelForm
from myapp.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['event']
        #event_time=forms.DateTimeField(widget=forms.DateTimeInput(format='%m/%d/%y',attrs={'class':'datetimepicker'}),
        #input_formats=('%m/%d/%y'))
class DoneForm(ModelForm):
    class Meta:
        model=Todo
        fields=['done']
