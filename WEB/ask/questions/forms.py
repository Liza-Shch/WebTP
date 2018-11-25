from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required True);
    password = forms.CharField(
        required True,
        widget=forms.PasswordInput()
    )

    #def clean(self):
        pass

    class QuestionForm(forms.ModelForm):
        class Meta:
            model = QuestionForm
            fields = ['title', 'text']
        def __init__(self, author, *args, **kwargs):
            self.aithor = author
            super().__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super.save(commit=False)
            obl.author = self.author
            if commit:
                obj.save
            return obj
    