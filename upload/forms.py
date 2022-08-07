from django import forms
from .models import Document


class DocumentAddForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'author', 'email1', 'email2', 'email3', 'email4', 'email5', 'pdf')
