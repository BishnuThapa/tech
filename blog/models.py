from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    featured_image = models.ImageField(upload_to='blog')
    description = models.TextField()
    readtime = models.CharField(
        max_length=10, help_text='eg: 5 min', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
