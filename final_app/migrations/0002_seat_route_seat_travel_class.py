# Generated by Django 5.1.3 on 2024-12-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='route',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='travel_class',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
