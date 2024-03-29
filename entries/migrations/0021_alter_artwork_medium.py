# Generated by Django 3.2.13 on 2022-05-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0020_auto_20220506_1024"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artwork",
            name="medium",
            field=models.CharField(
                choices=[
                    ("Painting", "PAINTING"),
                    ("Sculpture", "SCULPTURE"),
                    ("Photography", "PHOTO"),
                    ("Ceramic", "CERAMIC"),
                    ("Textile", "TEXTILE"),
                    ("Print", "PRINT"),
                    ("Digital", "DIGITAL"),
                    ("Other", "OTHER"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
