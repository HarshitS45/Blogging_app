from django import forms
from .models import BlogPost


class CreateBlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ('title', 'body', 'image')
    instance = ""
class UpdateBlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost

        fields = ('title', 'body', 'image')

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data.get('title')
        blog_post.body = self.cleaned_data.get('body')
        
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data.get('image')

        if commit:
            blog_post.save()

        return blog_post