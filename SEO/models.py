from django.db import models
from .models import *
# Create your models here.


class Seo(models.Model):

    meta_title = models.CharField(
        max_length=255, default='', null=True, blank=True)
    meta_keyword = models.CharField(
        max_length=255, default='', null=True, blank=True)
    meta_description = models.TextField(default='', null=True, blank=True)

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'
