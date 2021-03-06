# Generated by Django 3.0.4 on 2020-03-26 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
