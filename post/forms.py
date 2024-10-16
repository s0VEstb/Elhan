from django import forms
from .models import Post, Tag, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'category', 'tag', 'image']

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate > 5 or rate < 1:
            raise forms.ValidationError('Invalid rate')
        return rate


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {'name': 'Название',
                  'description': 'Описание'}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description']
        labels = {'name': 'Название',
                  'description': 'Описание'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Комментарий'}