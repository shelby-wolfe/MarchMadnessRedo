from django.contrib import admin
from .models import Team, Matchup, UserBracket, UserPick

admin.site.register(Team)
admin.site.register(Matchup)
admin.site.register(UserBracket)
admin.site.register(UserPick)
