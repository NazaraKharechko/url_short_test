# Generated by Django 3.1.6 on 2021-02-09 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urldata',
            options={'verbose_name': 'url', 'verbose_name_plural': 'urls'},
        ),
        migrations.AlterModelTable(
            name='urldata',
            table='url_data',
        ),
    ]
