from django import forms
from .models import User, Employee


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'password': forms.PasswordInput(),  # This hides the input value
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'salary', 'manager']


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['manager']  # Only allow the manager field to be updated
        widgets = {
            'manager': forms.Select(attrs={'class': 'form-control'}),
        }
