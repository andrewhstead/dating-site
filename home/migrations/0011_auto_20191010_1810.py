# Generated by Django 2.2.4 on 2019-10-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191010_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='priority',
            field=models.IntegerField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default=2, null=True),
        ),
    ]