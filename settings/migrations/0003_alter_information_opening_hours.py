# Generated by Django 4.2.2 on 2023-06-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_information_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='opening_hours',
            field=models.CharField(max_length=255),
        ),
    ]
