# Generated by Django 2.2.4 on 2019-10-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191010_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='priority',
            field=models.CharField(blank=True, choices=[(3, 'Low'), (2, 'Medium'), (1, 'High')], default='Medium', max_length=25, null=True),
        ),
    ]
