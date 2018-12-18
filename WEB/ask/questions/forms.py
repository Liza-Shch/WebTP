from django import forms
from questions.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import re

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password and confirm password does not match", code='invalid_password',)
        return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(max_length=100, required=False)
    #avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['nickname']

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder' : "Enter a title..."}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Enter a question..."}))
    tags = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder' : "Enter tags through the space..."}))

    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']

    def __init__(self, author, *args, **kwargs):
        self.author = author
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(QuestionForm, self).save(commit=False)
        obj.author = self.author
        obj.date_published = timezone.now()
        obj.is_published = True
        tag_list = self.cleaned_data['tags'].split(' ')
        tag_list = re.findall(r"[\w']+", self.cleaned_data['tags'])
        tag_objects = []
        for tag in tag_list:
            tag_object = Tag.objects.all().get(tag=tag)
            #raise forms.DoesNotExist("This tag does not exist", code='invalid tag',)
            tag_objects.append(tag_object)
        if commit:
            obj.save()
            for tag in tag_objects:
                obj.tag_set.add(tag)
        return obj

class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Enter your answer..."}))

    class Meta:
        model = Answer
        fields = ['text']

    def __init__(self, author, question, *args, **kwargs):
        self.author = author
        self.question = question
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(AnswerForm, self).save(commit=False)
        obj.author = self.author
        obj.correct = False
        obj.date_published = timezone.now()
        obj.question = self.question
        if commit:
            obj.save()
        return obj 