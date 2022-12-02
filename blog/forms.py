from django import forms
from .models import Post,PreviousPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Untitled'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Untitled'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'})
        }

class PrevUpdateForm(forms.ModelForm):
    class Meta:
        model = PreviousPost
        fields = ('title', 'body')

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Untitled'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'})
        }

