from django import forms
from .models import Links
#Essa class representa o formulário
class FormLinks(forms.ModelForm):
    class Meta:
        model = Links
        fields = "__all__"