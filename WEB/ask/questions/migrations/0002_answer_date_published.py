# Generated by Django 2.1.2 on 2018-12-11 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published'),
            preserve_default=False,
        ),
    ]
