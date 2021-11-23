from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Match, Game


def index(request):
    matches = []

    for match in Match.objects.all():
        winners = []
        for member in match.members.all():
            if member.place == 1:
                winners.append(member.player)

        matches.append({
            'game': match.game,
            'timestamp': match.timestamp,
            'winners': winners,
        })

    context = {
        'matches': matches,
    }

    return render(request, './index.html', context)


class GamesView(ListView):
    model = Game
    template_name = './games.html'
    context_object_name = 'games'


class GameView(DetailView):
    model = Game
    template_name = './game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = []

        for match in context['game'].matches.all():
            winners = []
            for member in match.members.all():
                if member.place == 1:
                    winners.append(member.player)

            matches.append({
                'timestamp': match.timestamp,
                'winners': winners,
            })

        context['matches'] = matches
        return context

