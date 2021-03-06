# Generated by Django 2.2.4 on 2020-05-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200506_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='denomination',
            field=models.CharField(choices=[('Catholic', 'Catholic'), ('Anglican', 'Anglican'), ('Methodist', 'Methodist'), ('Baptist', 'Baptist')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='diet',
            field=models.CharField(choices=[('Meat Eater', 'Meat Eater'), ('Vegetarian', 'Vegetarian'), ('Pescatarian', 'Pescatarian'), ('Vegan', 'Vegan')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='drinks',
            field=models.CharField(choices=[('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially'), ('Often', 'Often')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Asian', 'Asian')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='eyes',
            field=models.CharField(choices=[('Brown', 'Brown'), ('Blue', 'Blue'), ('Green', 'Green'), ('Grey', 'Grey'), ('Other', 'Other')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='hair',
            field=models.CharField(choices=[('Black', 'Black'), ('Brown', 'Brown'), ('Blonde', 'Blonde'), ('Red', 'Red'), ('Grey', 'Grey'), ('Bald', 'Bald'), ('Other', 'Other')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_children',
            field=models.CharField(choices=[('Yes, living with me', 'Yes, living with me'), ('Yes, living elsewhere', 'Yes, living elsewhere'), ('Yes, but grown-up', 'Yes, but grown-up'), ('No', 'No')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='looking_for',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='relationship',
            field=models.CharField(choices=[('Friendship', 'Friendship'), ('Fellowship', 'Fellowship'), ('Marriage', 'Marriage')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='smokes',
            field=models.CharField(choices=[('Never', 'Never'), ('Occasionally', 'Occasionally'), ('Often', 'Often')], default='-', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wants_children',
            field=models.CharField(choices=[('No', 'No'), ('One or Two', 'One or Two'), ('Lots', 'Lots'), ('Undecided', 'Undecided')], default='-', max_length=25, null=True),
        ),
    ]
