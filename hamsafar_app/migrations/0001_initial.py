# Generated by Django 5.0 on 2024-11-10 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamsafar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('seats', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hamsafars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
