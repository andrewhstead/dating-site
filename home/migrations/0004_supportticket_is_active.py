# Generated by Django 2.2.4 on 2019-10-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191010_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportticket',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
