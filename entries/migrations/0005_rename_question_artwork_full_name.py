# Generated by Django 3.2.13 on 2022-04-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0004_artwork_year_completed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artwork",
            old_name="question",
            new_name="full_name",
        ),
    ]
