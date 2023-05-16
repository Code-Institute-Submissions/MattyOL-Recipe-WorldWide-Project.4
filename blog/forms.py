from .models import Comment, Post, Category
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )


class AddForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'featured_image', 'slug', 'description', 'ingredients', 'content_image', 'method', 'category')
