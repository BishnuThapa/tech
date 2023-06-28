from django.db import models

# Create your models here.


class FooterInfo(models.Model):

    footer_logo = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    about_company = models.TextField(max_length=255)
    copyright_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_company

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'


class QuickLinks(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    serial_no = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Quick Links'
        verbose_name_plural = 'Quick Links'
