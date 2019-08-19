# Generated by Django 2.2.4 on 2019-08-15 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagethread',
            name='person_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads_started', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messagethread',
            name='person_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='contacts.MessageThread')),
            ],
        ),
    ]