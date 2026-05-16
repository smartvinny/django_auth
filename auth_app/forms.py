from django import forms

# TODO:IMPLEMENT ModelForm Later

class SignUpForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()
  phone = forms.CharField()
  password = forms.CharField(widget = forms.PasswordInput)
  password_confirm = forms.CharField(widget = forms.PasswordInput, label = "Confirm Password")


  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    password_confirm = cleaned_data.get("password_confirm")
    if password and password_confirm:
     if password != password_confirm:
      raise forms.ValidationError("Passwords do not match")
    return cleaned_data