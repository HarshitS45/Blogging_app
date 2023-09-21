import email
from django.core import exceptions
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django import forms
from .models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    """The form for registering an account."""
    email = forms.EmailField(max_length=50, help_text='Provide a valid email address.')
    class Meta():
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    """The form to for logging in."""
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    class Meta():
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email').lower()
            password = self.cleaned_data.get('password')

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid login details.")


class AccountUpdateForm(forms.ModelForm):
    """The form for updating the user details in the database"""
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()

        try:
            # Ckecking if this email does not already exist in the database
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f"Email: {email}, is alredy in use.")

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            # Ckecking if this username does not already exist in the database
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError(f'Username: {username}, is already in use.')
class SetPasswordForm(forms.Form):
    # …
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': 'true',
        'íd': 'new_password1',
        'name': 'new_password1',
    }))
    new_password2 = forms.CharField(label='Conform Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'required': 'true',
        'íd': 'new_password2',
        'name': 'new_password2',
    }))