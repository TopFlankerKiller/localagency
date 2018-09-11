from .models import User,Occupation,Userhasoccupation
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','lastname','email']




class OccupationForm(ModelForm):
    class Meta:
        model = Occupation
        fields = ['occupation']




class UserhasoccupationForm(ModelForm):
    class Meta:
        model = Userhasoccupation
        fields = ['user_id','occup_id']