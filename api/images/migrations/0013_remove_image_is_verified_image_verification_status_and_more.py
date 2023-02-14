# Generated by Django 4.1.5 on 2023-02-10 05:39

import django.contrib.postgres.fields
from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0012_image_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="is_verified",
        ),
        migrations.AddField(
            model_name="image",
            name="verification_status",
            field=models.CharField(
                choices=[
                    ("not_reviewed", "Not Reviewed"),
                    ("on_review", "On Review"),
                    ("declined", "Declined"),
                    ("verified", "Verified"),
                ],
                default="not_reviewed",
                help_text="The image's verification status.",
                max_length=12,
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="dominant_color",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.SmallIntegerField(),
                blank=True,
                null=True,
                size=3,
                validators=[images.models.Image.validate_rgb_value],
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="primary_color",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.SmallIntegerField(),
                blank=True,
                null=True,
                size=3,
                validators=[images.models.Image.validate_rgb_value],
            ),
        ),
    ]
