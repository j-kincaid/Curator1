# Generated by Django 3.2.13 on 2022-04-24 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0012_auto_20220424_1449"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artwork",
            old_name="depth",
            new_name="depth_in_inches",
        ),
        migrations.RenameField(
            model_name="artwork",
            old_name="height",
            new_name="height_in_inches",
        ),
        migrations.RenameField(
            model_name="artwork",
            old_name="width",
            new_name="width_in_inches",
        ),
    ]
