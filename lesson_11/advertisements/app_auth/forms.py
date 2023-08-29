from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Логин", min_length=6, max_length= 64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', max_length= 64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Фамилия', max_length= 64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Потверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def check_username(self):
        username = self.cleaned_data['username']
        username_check = User.objects.filter(username = username)
        if username_check.count():
            raise ValidationError("Логин уже занят")
        return username
    
    def check_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commint=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            first_name = self.cleaned_data['name'],
            last_name = self.cleaned_data['surname'],
            password = self.cleaned_data['password1']
        )
        return user