# Generated by Django 4.1.2 on 2022-11-01 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]
