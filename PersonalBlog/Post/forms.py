from django import forms
from .models import Postathomepage

class createpostform(forms.ModelForm):

    class Meta:
        model = Postathomepage
        fields = ('title','image','description')
