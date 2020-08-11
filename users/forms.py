
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from .models import Profile



class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email).exists():
            msg = ("لايوجد مستخدم بهذا البريد الالكتروني")
            self.add_error('email', msg)
        return email


class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields = ['username','email']
    def validate_password(self, value: str) -> str:
        return make_password(value)

class DateInput(forms.DateInput):
    input_type = 'date'

class AddInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput()
        }
        exclude = ['user','notes']


