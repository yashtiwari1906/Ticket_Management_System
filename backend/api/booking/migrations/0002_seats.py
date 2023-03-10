# Generated by Django 4.1.6 on 2023-02-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('booked', models.BooleanField()),
            ],
        ),
    ]
