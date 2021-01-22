from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
   # this class gives nested namespace  for configuration
    # forms.save() is called User model got these information which got
    class Meta:
        model = User
        fields= ['username', 'email', 'password1','password2']