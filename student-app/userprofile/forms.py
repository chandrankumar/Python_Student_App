from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserExtCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.CharField(max_length=15, required=True)
    username = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        
        if commit:
            user.save()
        return user

class UserProfilerForm(forms.ModelForm):
     class Meta:
            model = UserProfile
            fields = ('qualification','mobile')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    