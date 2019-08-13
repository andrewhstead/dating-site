# Generated by Django 2.2.4 on 2019-08-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190812_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='denomination',
            field=models.CharField(blank=True, choices=[('Catholic', 'Catholic'), ('Anglican', 'Anglican'), ('Methodist', 'Methodist'), ('Baptist', 'Baptist')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Asian', 'Asian')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='eyes',
            field=models.CharField(blank=True, choices=[('Brown', 'Brown'), ('Blue', 'Blue'), ('Green', 'Green'), ('Grey', 'Grey'), ('Other', 'Other')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='hair',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Brown', 'Brown'), ('Blonde', 'Blonde'), ('Red', 'Red'), ('Grey', 'Grey'), ('Bald', 'Bald'), ('Other', 'Other')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='looking_for',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Friendship', 'Friendship'), ('Fellowship', 'Fellowship'), ('Marriage', 'Marriage')], max_length=25, null=True),
        ),
    ]
