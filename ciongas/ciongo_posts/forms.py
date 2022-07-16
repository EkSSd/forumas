from django import forms
from . models import Post, Comment
from tinymce.widgets import TinyMCE


# cia kad pridedant savo posta, editori (jei taip galima pavadint) su'bootstrapintas butu






class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'post_image', 'content')
        exclude = ['author']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.HiddenInput(),
            'content': TinyMCE(),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'post_image', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': TinyMCE(),
            

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')
        exclude = ['user']
        widgets = {
            # 'user' : forms.HiddenInput(),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
        }
