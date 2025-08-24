from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):    
    class Meta:
        model = Task
        fields = ['title',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control rounded-4', 
            'name': 'title',
            'placeholder': 'enter the title',
            })