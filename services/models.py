from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    featured_image = models.ImageField(upload_to='services')
    icon = models.ImageField(upload_to='services',
                             help_text='Icon file 64*64 px', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Our Services'
