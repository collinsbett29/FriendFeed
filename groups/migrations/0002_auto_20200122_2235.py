# Generated by Django 3.0.2 on 2020-01-22 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collection',
            new_name='Group',
        ),
    ]