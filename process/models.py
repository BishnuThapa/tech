from django.db import models

# Create your models here.


class Process(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(help_text='icon file', default='')
    description = models.TextField()
    ordering = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'How It Works'
        verbose_name_plural = 'How It Works'
