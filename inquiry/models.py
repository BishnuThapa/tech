from django.db import models

# Create your models here.


class Inquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Customer Inquiry'
        verbose_name_plural = 'Customer Inquiries'
