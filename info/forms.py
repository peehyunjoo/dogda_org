from django import forms
from .models import dogda_info,dogda_vaccination_info,notice, diary

class Dogda_infoForm(forms.ModelForm):
    class Meta:
        model = dogda_info
        fields = ('id','dogda_name','dogda_birth','dogda_gender','dogda_type','reg_date')

class Dogda_vaccination_infoForm(forms.ModelForm):
    class Meta:
        model = dogda_vaccination_info
        fields = ('id','dogda_name','type','vaccination_date','reg_date')

class noticeForm(forms.ModelForm):
    class Meta:
        model = notice
        fields = ('title','content')
class diaryForm(forms.ModelForm):
    class Meta:
        model = diary
        fields = ('title','dogda_name','title','content','flowers','reg_date')


