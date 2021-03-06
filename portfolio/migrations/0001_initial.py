# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentUserHolding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=120, null=True)),
                ('current_holdings', models.FloatField(default=10000.0)),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_id', models.CharField(blank=True, max_length=120, null=True)),
                ('user_id', models.CharField(blank=True, max_length=120, null=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.CharField(max_length=120)),
                ('transaction', models.CharField(choices=[('SL', 'Sell'), ('BY', 'Buy')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserHolding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=120, null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('holdings', models.FloatField(default=10000.0)),
            ],
        ),
    ]
