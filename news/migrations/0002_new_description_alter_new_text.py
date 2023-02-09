# Generated by Django 4.1.6 on 2023-02-08 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='description',
            field=models.CharField(default='Null', max_length=50000, unique=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.CharField(max_length=5000),
        ),
    ]
