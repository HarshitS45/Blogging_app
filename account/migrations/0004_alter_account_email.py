# Generated by Django 4.0.2 on 2022-03-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_first_name_remove_account_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
