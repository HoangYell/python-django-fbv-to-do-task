from django import forms
from app_one.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'work_name': forms.TextInput(attrs={'class': 'textinputclass'}),
        }
