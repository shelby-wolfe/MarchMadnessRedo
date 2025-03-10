from django.shortcuts import render
from .models import Matchup

# Create your views here.

def bracket_view(request):
    # Get Matchups groups by region
    regions = ["East", "West", "Midwest", "South"]
    matchups_by_region = {region: Matchup.objects.filter(team1__region=region, round_number=1) for region in regions}

    return render(request, "bracket/bracket.html", {"matchups_by_region": matchups_by_region})