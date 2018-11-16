from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "autor",
            "title",
            "content"
        ]
        widgets={
            "autor": forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            "title": forms.TextInput(attrs={'class':'form-control'})
        }

