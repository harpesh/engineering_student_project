# Generated by Django 5.0.4 on 2024-04-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('joinig_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city_name', models.CharField(max_length=15)),
            ],
        ),
    ]