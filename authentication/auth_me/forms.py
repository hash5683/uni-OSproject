from django import forms
from django.contrib.auth.models import User

# Forms for user authentication and registration

class SignUpForm(forms.ModelForm):
    """
    A form for user signup. Collects username, email, password, and confirm_password.
    Ensures password and confirm_password match.
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'custom-input'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'custom-input'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'custom-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'custom-input'
            }),
        }

    def clean(self):
        """
        Validates that the password and confirm_password fields match.
        Raises a validation error if they do not.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    """
    A form for user login. Collects username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'custom-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'custom-input'
        })
    )
