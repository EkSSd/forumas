from django import forms
from . models import Puslapis, Tagg
from tinymce.widgets import TinyMCE


# cia kad pridedant savo posta, editori (jei taip galima pavadint) su'bootstrapintas butu






class PostForm(forms.ModelForm):
    class Meta:
        model = Puslapis
        fields = ('title', 'tag', 'content')
        exclude = ['author']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.HiddenInput(),
            'content': TinyMCE(),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Puslapis
        fields = ('title', 'tag', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),

        }
