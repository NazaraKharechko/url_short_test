# Generated by Django 3.1.6 on 2021-02-10 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0002_auto_20210209_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urldata',
            name='slug',
        ),
        migrations.AddField(
            model_name='urldata',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urldata',
            name='usage_count',
            field=models.PositiveIntegerField(default=None),
        ),
    ]