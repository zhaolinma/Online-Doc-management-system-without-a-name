from django.contrib.auth.models import User
from django import forms


class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password',]
    password = forms.CharField(widget=forms.PasswordInput)

