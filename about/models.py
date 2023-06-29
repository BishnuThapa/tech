from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    featured_image = models.ImageField(help_text='450*450 px', default='')
    featured_image1 = models.ImageField(help_text='450*450 px', default='')
    introduction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'About us'


class Goal(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Goals'
        verbose_name_plural = 'Goals'


class DirectorMessage(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    featured_image = models.ImageField(
        upload_to='team', null=True, blank=True, help_text='450*450 px')
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Director\'s Message'
        verbose_name_plural = 'Director\'s Message'
