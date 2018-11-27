# Generated by Django 2.1.2 on 2018-11-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(verbose_name='Correct'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(default=0, verbose_name='Object id'),
        ),
        migrations.AlterField(
            model_name='like',
            name='votes',
            field=models.IntegerField(choices=[(-1, 'dislike'), (1, 'like')], default=0, verbose_name='Votes'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name='Nickname'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(verbose_name='Is published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=50, verbose_name='Tag'),
        ),
    ]