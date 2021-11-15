# Generated by Django 3.2.9 on 2021-11-15 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('players', models.CharField(max_length=255, verbose_name='Количество игроков')),
                ('rules', models.TextField(verbose_name='Пользовательские правила')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(verbose_name='Продолжительность игры')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Время проведения')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.game', verbose_name='Игра')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('login', models.EmailField(max_length=254, verbose_name='Email')),
                ('fname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='MemberList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.match', verbose_name='Матч')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.user', verbose_name='Участник')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.user', verbose_name='Победитель'),
        ),
    ]