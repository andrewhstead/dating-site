# Generated by Django 2.2.4 on 2019-08-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190811_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]