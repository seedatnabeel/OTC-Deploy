from django import forms
from .models import Post

class PostForm(forms.ModelForm):
 #   box = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "name",
            "email",
            "comment"
        ]