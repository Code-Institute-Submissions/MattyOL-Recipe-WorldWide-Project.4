from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )


class AddForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'content_image', 'slug', 'recipe', 'category')
