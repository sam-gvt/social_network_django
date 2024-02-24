from .models import Post
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class PostCreateForm(forms.ModelForm):

    content = SummernoteTextField()


    class Meta:
        model = Post
        fields = ('title', 'caption', 'image', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-5'
            }),
            'caption': forms.TextInput(attrs={
                'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-5'
            }),
            
        }

    