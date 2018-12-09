# Generated by Django 2.1.2 on 2018-12-09 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventrun',
            name='happens',
        ),
        migrations.AddField(
            model_name='eventrun',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventrun',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
