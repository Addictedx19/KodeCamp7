# Generated by Django 4.0.5 on 2022-06-11 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_bio_people_alter_doctor_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='People',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
    ]