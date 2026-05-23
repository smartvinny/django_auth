from django import forms
from .models import CustomUser

# TODO:IMPLEMENT ModelForm Later

class SignUpForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()
  phone = forms.CharField()
  password = forms.CharField(widget = forms.PasswordInput)
  password_confirm = forms.CharField(widget = forms.PasswordInput, label = "Confirm Password")


  def clean_username(self):
    username = self.cleaned_data.get("username")
    if CustomUser.objects.filter(username__iexact = username).exists():
      raise forms.ValidationError("Username already exists")
    return username
  
  def clean_email(self):
    email = self.cleaned_data.get("email")
    if CustomUser.objects.filter(email__iexact = email).exists():
      raise forms.ValidationError("Email already exists")
    return email


  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    password_confirm = cleaned_data.get("password_confirm")
    if password and password_confirm:
     if password != password_confirm:
      raise forms.ValidationError("Passwords do not match")
    return cleaned_data