from django.contrib import admin
from .models import VotingData, VoterDataAccess
# Register your models here.

admin.site.register(VotingData)
admin.site.register(VoterDataAccess)
