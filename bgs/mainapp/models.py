from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, verbose_name='Изображение')
    # todo: whitelist
    # todo: blacklist

    def __str__(self):
        return f'{self.user.username} ({self.user.first_name} {self.user.last_name})'


class Game(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    players = models.CharField(max_length=255, verbose_name='Количество игроков')
    rules = models.TextField(blank=True, verbose_name='Пользовательские правила')
    image = models.ImageField(verbose_name='Изображение')
    # todo: rating

    def __str__(self):
        return self.name


class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра', related_name='matches')
    duration = models.DurationField(verbose_name='Продолжительность игры')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время проведения')

    def __str__(self):
        # todo формат дата
        return f'{self.game.name} ({self.timestamp})'


class Member(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name='Матч', related_name='members')
    player = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Участник', related_name='matches')
    place = models.PositiveSmallIntegerField(verbose_name='Место')

    def __str__(self):
        return f'{self.player.user.username} - {self.match.game.name} ({self.place})'
