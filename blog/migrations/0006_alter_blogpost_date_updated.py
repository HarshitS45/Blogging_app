# Generated by Django 4.0.2 on 2022-04-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
    ]
