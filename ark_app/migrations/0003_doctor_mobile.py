# Generated by Django 4.0.4 on 2022-11-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ark_app', '0002_doctor_isactive_patient_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
