from django import forms
from .models import Post

class PostForm(forms.ModelForm):
   # Cough = forms.BooleanField()
    Cough = forms.BooleanField()
    Fever = forms.BooleanField()
    Runny_Nose = forms.BooleanField()
    Nasal_Congestion = forms.BooleanField()

    class Meta:
        model =Post
        fields= [
            "title",
            "content"
        ]