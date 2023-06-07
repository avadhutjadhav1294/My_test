from django import forms
from library import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        exclude = ["is_active",]