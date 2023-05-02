from django import forms
from .models import Posts

# class CreatePost(forms.Form):
#     title = forms.CharField(label="Title", max_length=150, required=True)
#     content = forms.CharField(label="Content", required=True)
#     # content = forms.Textarea(label="Content")

class StudentModelForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['title','content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }