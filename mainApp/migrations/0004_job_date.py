# Generated by Django 3.1.7 on 2021-04-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
