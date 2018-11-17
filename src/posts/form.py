from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image"
        ]
        widgets={
            'content': forms.Textarea(attrs={'class':'form-control','required':'true'}),
            "title": forms.TextInput(attrs={'class':'form-control','required':'true'}),
            "image": forms.FileInput(attrs={'class':'form-control','required':'true'})
        }




