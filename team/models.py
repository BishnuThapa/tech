from django.db import models

# Create your models here.


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)

    # file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30
    # photo = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    photo = models.ImageField(upload_to='team')  # "team"
    order_no = models.IntegerField(default=1, null=True, blank=True)
    facebook_link = models.URLField(
        null=True, blank=True, default="facebook.com")
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
