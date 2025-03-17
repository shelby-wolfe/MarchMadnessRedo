from django.db import models
from django.contrib.auth.models import User 

class Team(models.Model):
    name = models.CharField(max_length=100)
    seed = models.IntegerField() # Seed Number (1-16)
    region = models.CharField(max_length=50) #East, West, MidWest, South
    
    def __str__(self):
        return f"{self.name} ({self.seed}) - {self.region}"
    
class Matchup(models.Model):
    round_number = models.IntegerField() # 1 = First Round, 2=Second, etc...
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matchups')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matchups')
    winner= models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_matchups')
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Round {self.round_number}: {self.team1} vs {self.team2}"
    
class UserBracket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Bracket"
    
class UserPick(models.Model):
    bracket = models.ForeignKey(UserBracket, on_delete=models.CASCADE)
    matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
    selected_winner = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bracket.user.username} - {self.matchup} Pick: {self.selected_winner}"