from django import forms
from .models import Todo


class ListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...', 'class': 'form-control'}))
    class Meta:
        model = Todo
        fields = '__all__'
