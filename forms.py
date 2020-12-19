from django import forms
from .models import ram
class frm(forms.ModelForm):
    class Meta:
        model = ram
     
        fields = "__all__"
