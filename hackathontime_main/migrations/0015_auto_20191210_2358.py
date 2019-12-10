# Generated by Django 2.2.7 on 2019-12-10 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0017_team_team_slug'),
        ('hackathontime_main', '0014_hackathon_hackathon_won'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_runnerup_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='++', to='hackathontime_users.Team'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_runnerup_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='++', to='hackathontime_users.Team'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_location_url',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
