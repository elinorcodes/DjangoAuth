from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    CHOICES = (('A', 'A'),('B', 'B'))
    group = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = User
        fields = ('username', 'group', 'password1', 'password2')

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)