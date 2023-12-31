# Generated by Django 4.1.5 on 2023-08-31 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_booth_number', models.IntegerField()),
                ('polling_booth_name', models.CharField(max_length=100)),
                ('parent_constituency', models.CharField(max_length=100)),
                ('winner_2014', models.CharField(max_length=100)),
                ('first_runner_up_other_than_INC_and_BJP', models.CharField(blank=True, max_length=100, null=True)),
                ('margin_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('margin', models.IntegerField(blank=True, null=True)),
                ('total_voters', models.IntegerField()),
                ('bjp_votes', models.IntegerField(blank=True, null=True)),
                ('bjp_vote_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inc_votes', models.IntegerField(blank=True, null=True)),
                ('inc_vote_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoterDataAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Assam', 'Assam'), ('Andhra Pradesha', 'Andhra Pradesha'), ('Madhya Pradesh ', 'Madhya Pradesh '), ('Uttar Pradesh ', 'Uttar Pradesh '), ('Chhattisgarh', 'Chhattisgarh'), ('Gujarat', 'Gujarat'), ('Maharashtra', 'Maharashtra'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Mizoram ', 'Mizoram '), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Sikkim ', 'Sikkim '), ('Nagaland', 'Nagaland'), ('Rajasthan ', 'Rajasthan '), ('Manipur ', 'Manipur '), ('Haryana ', 'Haryana '), ('Orissa ', 'Orissa '), ('West Bengal ', 'West Bengal '), ('Meghalaya ', 'Meghalaya '), ('Kerala ', 'Kerala '), ('Uttarakhand ', 'Uttarakhand '), ('Himachal Pradesh', 'Himachal Pradesh'), ('Tamil Nadu ', 'Tamil Nadu '), ('Punjab ', 'Punjab '), ('Goa', 'Goa'), ('Tripura ', 'Tripura '), ('Karnataka ', 'Karnataka '), ('Bihar ', 'Bihar '), ('Telangana ', 'Telangana ')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
