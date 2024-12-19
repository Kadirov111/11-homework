# Generated by Django 5.1.4 on 2024-12-19 17:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('short_content', models.TextField()),
                ('long_content', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
