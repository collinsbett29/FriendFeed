# Generated by Django 3.0.2 on 2020-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200123_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.CharField(max_length=200),
        ),
    ]
