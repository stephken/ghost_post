from django.db import models
from django.utils import timezone 
# Create your models here.

class Roast_Boast(models.Model):
    POST_CHOICE = ((True, 'Boast'), (False, 'Roast'))

    user_input = models.CharField(max_length=200)
    boast = models.BooleanField(choices=POST_CHOICE)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)

    @property
    def count_votes(self):
        return self.up_vote + self.down_vote
    

