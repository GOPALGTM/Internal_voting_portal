from django import forms
from .models import VotingData

class VotingForm(forms.ModelForm):
    class Meta:
        model = VotingData
        fields = ["polling_booth_number", "polling_booth_name", "parent_constituency", "winner_2014", "first_runner_up_other_than_INC_and_BJP", "margin_percentage", "margin", "total_voters", "bjp_votes", "bjp_vote_percentage", "inc_votes", "inc_vote_percentage"]
        # widgets = {
        #     'polling_booth_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'polling_booth_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'parent_constituency': forms.TextInput(attrs={'class': 'form-control'}),
        #     'winner_2014': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_runner_up_other_than_INC_and_BJP': forms.TextInput(attrs={'class': 'form-control'}),
        #     'margin_percentage': forms.DecimalField(attrs={'class': 'form-control'}),
        #     'margin': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'total_voters': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'bjp_votes': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'bjp_vote_percentage': forms.DecimalField(attrs={'class': 'form-control'}),
        #     'inc_votes': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'inc_vote_percentage': forms.DecimalField(attrs={'class': 'form-control'}),
        # }
