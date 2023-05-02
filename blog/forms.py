from .models import Comment
from django import forms
from .models import AddModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )


class AddForm(forms.ModelForm):

    class Meta:
        model = AddModel
        fields = '__all__'
