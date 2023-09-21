from django.db import models
from django.utils.text import slugify
from django.conf import settings 
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from ckeditor.fields import RichTextField


def upload_location(instance, filename):
    """Generate the file path for image upload"""
    file_path = f'blog/{str(instance.author.id)}/{str(instance.title)}-{filename}'
    return file_path

class BlogPost(models.Model):
    """Creates these fields in the database which will all be the attributes of a post"""
    title                   = models.CharField(max_length=50, blank=False, null=False)
    body                    = RichTextField(max_length=10000, blank=False, null=False)
    # body                    = models.TextField(max_length=10000, blank=False, null=False)
    image                   = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published          = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated            = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True, max_length=255)


    def __str__(self):
        return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    """Deletes the image of a blog-post when the correlating BlogPost is deleted"""
    instance.image.delete(False)


def pre_save_blog_post_receiver(sender, instance, **kwargs):
    """Checks if a blog post has a slug, if not it creates one. This executes before each blog post is commited to the database"""
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)
pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)

