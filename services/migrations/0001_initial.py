# Generated by Django 4.2.2 on 2023-06-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('featured_image', models.ImageField(upload_to='services')),
                ('icon', models.ImageField(blank=True, help_text='Icon file 64*64 px', null=True, upload_to='services')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Our Services',
            },
        ),
    ]
