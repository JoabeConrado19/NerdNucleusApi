# Generated by Django 4.1.6 on 2023-05-18 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animesDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=5000)),
                ('thumb', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('ep', models.IntegerField()),
                ('srcMedium', models.CharField(max_length=5000, null=True)),
                ('srcHD', models.CharField(max_length=5000, null=True)),
                ('anime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eps', to='animesDetails.animedetails')),
            ],
        ),
    ]