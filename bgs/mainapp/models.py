from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    login = models.EmailField(verbose_name='Email')
    fname = models.CharField(max_length=50, verbose_name='Имя')
    lname = models.CharField(max_length=50, verbose_name='Фамилия')
    date_of_birth = models.DateField(blank=True, verbose_name='Дата рождения')
    image = models.ImageField(verbose_name='Изображение')
    # todo: whitelist
    # todo: blacklist


class Game(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    players = models.CharField(max_length=255, verbose_name='Количество игроков')
    rules = models.TextField(verbose_name='Пользовательские правила')
    image = models.ImageField(verbose_name='Изображение')
    # todo: rating


class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    duration = models.DurationField(verbose_name='Продолжительность игры')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время проведения')


class MemberList(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name='Матч')
    member = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Участник')
    place = models.PositiveSmallIntegerField(default=0, verbose_name='Место')
