# Generated by Django 5.2 on 2025-04-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_pawclock", "0004_created_day_care_session_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="daycaresession",
            name="check_in",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="daycaresession",
            name="check_out",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
