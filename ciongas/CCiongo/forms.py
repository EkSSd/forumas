# from django import forms
# from . models import Puslapis, Tagg


# # cia kad pridedant savo posta, editori (jei taip galima pavadint) su'bootstrapintas butu

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Puslapis
#         fields = ('title', 'tagas', 'author', 'content')

#         widgets = {
#             'title': forms.TextInput(attrs={'class':'form-control'}),
#             'author': forms.Select(attrs={'class':'form-control'}),
#             'content': forms.Textarea(attrs={'class':'form-control'}),

#         }

#         tagas = forms.ModelMultipleChoiceField(queryset = Tagg.objects.all(), widget = forms.CheckboxSelectMultiple),