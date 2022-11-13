# Generated by Django 4.0.4 on 2022-11-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ark_app', '0005_doctor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='default', upload_to='doctors/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(default='default', upload_to='patients/images/'),
            preserve_default=False,
        ),
    ]