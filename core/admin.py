from django.contrib import admin
from .models import Team, Player, TeamGroup, Coach

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(TeamGroup)
admin.site.register(Coach)
