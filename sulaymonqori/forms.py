from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from sulaymonqori.models import Post


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
