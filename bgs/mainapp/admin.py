from django.contrib import admin
from .models import Profile, Game, Match, Member

# Register your models here.
admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Match)
admin.site.register(Member)
