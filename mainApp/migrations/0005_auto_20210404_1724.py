# Generated by Django 3.1.7 on 2021-04-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_job_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='hr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.hruser'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
