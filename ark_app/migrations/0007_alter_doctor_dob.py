# Generated by Django 4.0.4 on 2022-11-13 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ark_app', '0006_doctor_image_patient_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now, null=True),
        ),
    ]
