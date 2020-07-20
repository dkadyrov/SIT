from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Art

class ArtForm(forms.ModelForm):
    image_1 = forms.FileField()
    image_2 = forms.FileField()

    class Meta:
        model = Art
        fields = ('title', 'image_1', 'image_2')


class CustomUserCreationForm(SignupForm):
    class Meta(SignupForm):
        model = User
        fields = ('username', 'email', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields



