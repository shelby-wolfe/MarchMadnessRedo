from django.core.management.base import BaseCommand
from bracket.models import Team

class Command(BaseCommand):
    help = "Seed the database with March Madness Teams"

    def handle(self, *args, **kwargs):
        teams = { 
            "East": [(1, "Team A"), (2, "Team B"), (3, "Team C"), (4, "Team D"),(5, "Team E"), (6, "Team F"), (7, "Team G"), (8, "Team H"), 
                     (9, "Team I"), (10, "Team J"), (11, "Team K"), (12, "Team L"), (13, "Team M"), (14, "Team N"), (15, "Team O"), (16, "Team P")],  
            "West": [(1, "Team Q"), (2, "Team R"), (3, "Team S"), (4, "Team T"),(5, "Team U"), (6, "Team V"), (7, "Team W"), (8, "Team X"), 
                     (9, "Team Y"), (10, "Team Z"), (11, "Team AA"), (12, "Team BB"), (13, "Team CC"), (14, "Team DD"), (15, "Team EE"), (16, "Team FF")],  
            "Midwest": [(1, "Team GG"), (2, "Team HH"), (3, "Team II"), (4, "Team JJ"),(5, "Team KK"), (6, "Team LL"), (7, "Team MM"), (8, "Team NN"),
                        (9, "Team OO"), (10, "Team PP"), (11, "Team QQ"), (12, "Team RR"), (13,"Team SS"), (14, "Team TT"), (15, "Team UU"), (16, "Team VV")],  
            "South": [(1, "Team WW"), (2, "Team XX"), (3, "Team YY"), (4, "Team ZZ"),(5, "Team AAA"), (6, "Team BBB"), (7, "Team CCC"), (8, "Team DDD"), 
                      (9, "Team EEE"), (10, "Team FFF"), (11, "Team GGG"), (12, "Team HHH"), (13, "Team III"), (14, "Team JJJ"), (15, "Team KKK"), (16, "Team LLL")] }
        
        for region in teams.keys():
            for seed in range(1, 17):
                Team.objects.get_or_create(name="TBD", seed=seed, region=region)

        self.stdout.write(self.style.SUCCESS("Successfully seeded teams!"))