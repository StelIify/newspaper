# Generated by Django 3.1.13 on 2021-12-03 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]