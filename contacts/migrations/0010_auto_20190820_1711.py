# Generated by Django 2.2.4 on 2019-08-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20190819_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wave',
            name='total_waves',
            field=models.IntegerField(default=0),
        ),
    ]