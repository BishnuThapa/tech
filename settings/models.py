from django.db import models

# Create your models here.


class Favicon(models.Model):
    name = models.CharField(max_length=255)
    favicon = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Favicon'


class Logo(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'


class Information(models.Model):
    website_title = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    secondary_email = models.EmailField(max_length=255, null=True, blank=True)
    opening_hours = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_title

    class Meta:
        verbose_name = 'Company Information'
        verbose_name_plural = 'Company Information'


class SocialLinks(models.Model):
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_title

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
