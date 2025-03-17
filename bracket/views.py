from django.shortcuts import render
from .models import Matchup

def generate_next_round():
    regions = ["East", "West", "South", "Midwest"]

    for region in regions:
        # Get the winners from Round 1 for this region
        round_1_matchups = Matchup.objects.filter(round_number=1, region=region)
        winners = []

        for matchup in round_1_matchups:
            if matchup.winner:
                winners.append(matchup.winner.id)  # Store team IDs only

        # Ensure we have exactly 16 winners (8 matchups)
        if len(winners) != 16:
            print(f"Error: Expected 16 winners for {region}, but found {len(winners)}")
            continue

        # Remove old Round 2 matchups before creating new ones
        Matchup.objects.filter(round_number=2, region=region).delete()

        # Create new matchups by pairing adjacent winners
        for i in range(0, 16, 2):
            team1_id = winners[i]
            team2_id = winners[i + 1]

            Matchup.objects.create(
                round_number=2,
                team1_id=team1_id,
                team2_id=team2_id,
                region=region,
            )


def bracket_view(request):
    # Fetch the matchups for round 1
    round_1_east = Matchup.objects.filter(region="East", round_number=1)
    round_1_west = Matchup.objects.filter(region="West", round_number=1)
    round_1_south = Matchup.objects.filter(region="South", round_number=1)
    round_1_midwest = Matchup.objects.filter(region="Midwest", round_number=1)

    # Automatically generate round 2 matchups if not already done
    generate_next_round()

    # Fetch the matchups for round 2
    round_2_east = Matchup.objects.filter(round_number=2, region="East")
    round_2_west = Matchup.objects.filter(round_number=2, region="West")
    round_2_south = Matchup.objects.filter(round_number=2, region="South")
    round_2_midwest = Matchup.objects.filter(round_number=2, region="Midwest")

    context = {
        "round_1_east": round_1_east,
        "round_1_west": round_1_west,
        "round_1_south": round_1_south,
        "round_1_midwest": round_1_midwest,
        "round_2_east": round_2_east,
        "round_2_west": round_2_west,
        "round_2_south": round_2_south,
        "round_2_midwest": round_2_midwest,
    }

    return render(request, "bracket/bracket.html", context)