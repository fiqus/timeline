# Generated by Django 2.2 on 2019-06-21 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timelineentry',
            options={'verbose_name_plural': 'timeline entries'},
        ),
    ]