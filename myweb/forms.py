
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User

# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import Comment2



class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [

                'username',
                'email',
                'password1',
                'password2'
        ]


class MyCommentForm2(ModelForm):
    class Meta:
        model = Comment2
        fields = ['id', 'User_Name', 'Phone', 'E_mail','A_ddess', 'P_code', 'N_slip']

