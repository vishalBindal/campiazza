from django.contrib.auth.models import User
from .models import Item,ItemImage, Profile
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']


class ImageForm(forms.ModelForm):
    image=forms.ImageField(required=False)

    class Meta:
        model=ItemImage
        fields=['image']


class ItemForm(forms.ModelForm):

    class Meta:
        model=Item
        fields = ['name', 'price', 'description', 'category', 'condition']


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'phone', 'address', 'profile_pic']
