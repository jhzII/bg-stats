# Generated by Django 3.2.9 on 2021-11-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='winner',
        ),
        migrations.AddField(
            model_name='memberlist',
            name='place',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Место'),
        ),
    ]