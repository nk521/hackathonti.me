# Generated by Django 2.2.7 on 2019-12-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_main', '0011_auto_20191210_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_location_name',
            field=models.CharField(default='No venue as of now.', max_length=255),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_location_url',
            field=models.URLField(default='null', max_length=255),
        ),
    ]