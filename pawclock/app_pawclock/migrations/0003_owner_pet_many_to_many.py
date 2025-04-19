# Generated by Django 5.2 on 2025-04-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pawclock', '0002_created_owner_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owners',
            field=models.ManyToManyField(related_name='pets', to='app_pawclock.owner'),
        ),
    ]
