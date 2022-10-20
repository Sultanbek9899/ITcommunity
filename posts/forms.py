from django import forms

from posts.models import Post, Comment


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


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description",]
        widgets = {
            "description": forms.Textarea(
                attrs={"class":"form-control"}
            )
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content":forms.TextInput(
                attrs={"class":"form-control"}
            )
        }