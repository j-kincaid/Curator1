# Generated by Django 3.2.13 on 2022-04-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0006_rename_full_name_artwork_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="artwork",
            name="dimensions",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="artwork",
            name="media",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
