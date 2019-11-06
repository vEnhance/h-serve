# Generated by Django 2.2.7 on 2019-11-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydrogen', '0007_auto_20191105_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_live_grading',
            field=models.BooleanField(default=True, help_text='Whether feedback should be shown instantly.'),
        ),
        migrations.AlterField(
            model_name='test',
            name='max_attempts',
            field=models.PositiveIntegerField(default=0, help_text="Number of available attempts on each problem on the test for live-grading. Set to zero if you don't want a limit."),
        ),
    ]
