from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class VotingData(models.Model):
    polling_booth_number = models.IntegerField()
    polling_booth_name = models.CharField(max_length=100)
    parent_constituency = models.CharField(max_length=100)
    winner_2014 = models.CharField(max_length=100)
    first_runner_up_other_than_INC_and_BJP = models.CharField(max_length=100, blank=True, null=True)
    margin_percentage = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    margin = models.IntegerField(blank=True, null=True)
    total_voters = models.IntegerField()
    bjp_votes = models.IntegerField(blank=True, null=True)
    bjp_vote_percentage = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)
    inc_votes = models.IntegerField(blank=True, null=True)
    inc_vote_percentage = models.DecimalField(max_digits=12, decimal_places=10, blank=True, null=True)

    def __str__(self):
        return f"Polling Booth {self.polling_booth_number}: {self.polling_booth_name}"
