# Generated by Django 2.2.4 on 2019-10-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191010_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 1), ('Medium', 2), ('High', 3)], default='Medium', max_length=25, null=True),
        ),
    ]