from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import*

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class ProfileForm(ModelForm):
    class Meta:
        model=Profiles
        fields=["isim","resim"]
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


