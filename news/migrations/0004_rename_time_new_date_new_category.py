# Generated by Django 4.1.6 on 2023-02-08 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_new_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='time',
            new_name='date',
        ),
        migrations.AddField(
            model_name='new',
            name='category',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
