from django.contrib import admin
from .models import User, Game, Match, MemberList

# Register your models here.
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Match)
admin.site.register(MemberList)
