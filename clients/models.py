from django.db import models

# Create your models here.


class Clients(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_logo = models.ImageField(
        upload_to='clients', blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
