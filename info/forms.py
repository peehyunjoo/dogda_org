from django import forms
from .models import dogda_info

class Dogda_infoForm(forms.ModelForm):
    class Meta:
        model = dogda_info
        fields = ('id','dogda_name','dogda_birth','dogda_gender','dogda_type','reg_date')