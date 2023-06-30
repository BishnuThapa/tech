from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    image = models.ImageField(help_text='icon file', default='')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
