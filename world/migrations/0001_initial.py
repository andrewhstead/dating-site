# Generated by Django 2.2.4 on 2019-08-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=25, unique=True)),
                ('abbreviation', models.CharField(max_length=3, unique=True)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='images/countries')),
            ],
        ),
    ]
