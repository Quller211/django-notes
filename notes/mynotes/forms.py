from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Notes
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class FormNote(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note_text']
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Название заметки',
                'width': '250px'}),
            'note_text': forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Текст заметки',
                'rows': 5,
                'cols': 10}),
        }
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Логин', 'class' : 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Пароль', 'class' : 'form-control'}))


class RegisterUser(UserCreationForm):

    username = forms.CharField(label = 'Имя пользователя', widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    password2 = forms.CharField(label = 'Повтор пароля', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')