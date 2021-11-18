from django.shortcuts import render
from .models import Match


def index(request):
    matches = []

    for match in Match.objects.all():
        winners = []
        for member in match.members.all():
            if member.place == 1:
                winners.append(member.member)

        matches.append({
            'game': match.game,
            'timestamp': match.timestamp,
            'winners': winners,
        })

    context = {
        'matches': matches,
    }

    return render(request, './index.html', context)
