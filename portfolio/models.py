from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    work = models.CharField(
        max_length=100, default='', null=True, blank=True, help_text='eg. Branding, Logo Design, Web Development')
    image = models.ImageField(upload_to='portfolio', help_text='400*400')
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'
