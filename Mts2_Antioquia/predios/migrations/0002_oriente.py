# Generated by Django 4.0.3 on 2022-03-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='oriente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stratum', models.IntegerField()),
                ('price', models.BigIntegerField()),
                ('mtsC', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]