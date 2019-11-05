# Generated by Django 2.2.7 on 2019-11-05 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(default='waaaaaa', unique=True, verbose_name='A slug for the URL for the about page.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(default='', help_text='A description about the contest. HTML OK.'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='group',
            field=models.ForeignKey(help_text='The group for users who are run this.', on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]