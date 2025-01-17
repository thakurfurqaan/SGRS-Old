from django import forms
from .models import Grievance, Reply
from redressal.models import SubCategory

class NewGrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['category','sub_category','subject','message','image']

class GrievanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['sub_category','subject','message','image','status']
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(),disabled=True)
    subject = forms.CharField(disabled=True)
    message = forms.CharField(disabled=True,widget=forms.Textarea)
    image= forms.ImageField(disabled=True,required=False)

class NewReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields= ['message','grievance']
    grievance = forms.ModelChoiceField(
            queryset=Grievance.objects.all(),
            widget=forms.HiddenInput())