from django import forms
from .models import Postathomepage
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class createpostform(forms.ModelForm):

    class Meta:
        model = Postathomepage
        fields = ('title','image','description')

class signupform(UserCreationForm):
    pass

class loginform(AuthenticationForm):
    pass