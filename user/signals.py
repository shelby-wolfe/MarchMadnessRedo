from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile 
from bracket.models import Matchup  # Corrected import for Matchup model from bracket.models

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

def generate_next_round(previous_round_number):
    # Fetch the previous round's matchups
    previous_round = Matchup.objects.filter(round_number=previous_round_number)
    next_round_number = previous_round_number + 1

    # Create matchups for the next round
    for i in range(0, len(previous_round), 2):
        if previous_round[i].winner and previous_round[i + 1].winner:
            # Create the next matchup between the winners of the previous round
            Matchup.objects.create(
                round_number=next_round_number,
                team1=previous_round[i].winner,
                team2=previous_round[i + 1].winner,
                region=previous_round[i].region,  # Assuming the same region as the previous round
            )