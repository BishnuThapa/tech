
from django.db import models

# Create your models here.


class Banner(models.Model):
    banner = models.ImageField(upload_to='banner',
                               help_text='1920*1280 px')
    thumbnail = models.ImageField(upload_to='banner')
    slogan = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    button_name = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner Setting'
