from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, WithdrawalTransaction, UserProfile
from django.contrib.auth import get_user_model

user = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # No user_type field

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'client'  # Automatically set user_type to 'client'
        if commit:
            user.save()
        return user

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = WithdrawalTransaction
        fields = ['crypto_type', 'withdrawal_address', 'amount']
        widgets = {
            'crypto_type': forms.Select(attrs={'class': 'form-control'}),
            'withdrawal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your withdrawal wallet address'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount to withdraw'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["first_name", "last_name", "email"]

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_picture"]