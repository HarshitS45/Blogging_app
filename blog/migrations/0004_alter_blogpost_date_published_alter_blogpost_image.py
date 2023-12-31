# Generated by Django 4.0.2 on 2022-04-06 10:35

import blog.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 6, 10, 35, 53, 897990, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]
