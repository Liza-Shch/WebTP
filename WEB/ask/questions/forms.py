from django import forms
from questions.models import *
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    nickname = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password', 'avatar']

    def clean(self):
        cdata = super(SignUpForm, self).clean()
        password = cdata['password']
        confirm_password = cdata['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password and confirm password does not match")
        return cdata

class SettingsForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(max_length=255, required=False)
    nickname = forms.CharField(max_length=100, required=False)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'avatar']

#class QuestionForm(forms.Form):
#    class Meta:
#        model = QuestionForm
#        fields = ['title', 'text']
#    def __init__(self, author, *args, **kwargs):
#        self.aithor = author
#        super().__init__(*args, **kwargs)

#    def save(self, commit=True):
#        obj = super.save(commit=False)
#        obl.author = self.author
#        if commit:
#            obj.save
#        return obj
    