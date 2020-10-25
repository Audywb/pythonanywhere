from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User

# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import Sell
from .models import Comment
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

# create a ModelForm 
class Sell(ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Sell
        fields = [
             'name',
             'p_number',
             'e_mail',
             'address',
             'postcode',
             'number_slip'
             
        ]

class MyCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['Name', 'Phone_Number', 'Email']

class MyCommentForm2(ModelForm):
    class Meta:
        model = Comment2
        fields = ['User_Name', 'Phone', 'E_mail','A_ddess', 'P_code', 'N_slip']