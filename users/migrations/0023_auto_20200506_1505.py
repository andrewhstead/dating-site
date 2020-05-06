# Generated by Django 2.2.4 on 2020-05-06 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200506_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(default='-', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='world.Country'),
        ),
    ]
