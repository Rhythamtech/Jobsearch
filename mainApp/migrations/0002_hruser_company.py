# Generated by Django 3.1.7 on 2021-04-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hruser',
            name='company',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
