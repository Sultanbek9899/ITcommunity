from django import forms

from posts.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = [
            "image",
            "description", 
        ]
        widgets = {
            "image": forms.FileInput(
                attrs = {"class":"form-control"},
            ),
            "description": forms.Textarea(
                attrs= {"class":"form-control"}
            )
        }
        labels = {
            "image": "Изображение",
            "description": "Описание публикации"
        }