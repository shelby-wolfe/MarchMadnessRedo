from bracket.models import Team, Matchup

regions = ["East", "West", "Midwest", "South"]

for region in regions:
    teams = Team.objects.filter(region=region).order_by("seed")
    matchups = [
        (teams[0], teams[15]), 
        (teams[1], teams[14]),
        (teams[2], teams[13]),
        (teams[3], teams[12]),
        (teams[4], teams[11]),
        (teams[5], teams[10]),
        (teams[6], teams[9]),
        (teams[7], teams[8]),
    ]
    
    for team1, team2 in matchups:
        Matchup.objects.get_or_create(round_number=1, team1=team1, team2=team2)

print("First-round matchups generated successfully!")