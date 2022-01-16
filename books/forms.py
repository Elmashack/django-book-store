from django import forms
from django.core import validators

from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Book Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Author', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(label='Price', widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Book cover', validators=[validators.FileExtensionValidator(
        allowed_extensions=('jpeg', 'jpg', 'png'))],
        error_messages={
            'invalid_extensions': "This format is not valid"
        }
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }
