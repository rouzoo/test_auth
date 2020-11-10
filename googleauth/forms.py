from .models import Profile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Электронная почта'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'pic')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].label = 'Информация о себе'
        self.fields['pic'].label = 'Изображение'
