from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    #avatar
    avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(max_value=100, min_value=0)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]
        username = cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой Никнейм уже есть, введите другое")
        if password != confirm_password:
            raise forms.ValidationError("Пароли не Совпадают !")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
