# Generated by Django 3.2.16 on 2023-01-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('sex', models.FloatField()),
                ('bmi', models.FloatField()),
                ('children', models.FloatField()),
                ('smoker', models.FloatField()),
                ('region', models.FloatField()),
                ('charges', models.FloatField()),
            ],
        ),
    ]
