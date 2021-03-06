# Generated by Django 3.0.2 on 2020-01-22 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('body', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('solved', models.BooleanField(default=False)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='groups.Collection')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question')),
            ],
            options={
                'ordering': ['-likes'],
            },
        ),
    ]
