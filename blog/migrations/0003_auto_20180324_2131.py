# Generated by Django 2.0.3 on 2018-03-24 13:31

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('blog', '0002_auto_20180323_0500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoty',
            new_name='Category',
        ),
    ]
