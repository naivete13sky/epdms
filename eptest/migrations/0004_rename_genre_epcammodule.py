# Generated by Django 4.1.3 on 2022-11-30 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eptest', '0003_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='EpcamModule',
        ),
    ]