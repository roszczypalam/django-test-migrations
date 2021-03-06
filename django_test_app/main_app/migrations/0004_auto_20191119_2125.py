# -*- coding: utf-8 -*-
# Generated by Django 2.2.7 on 2019-11-19 21:25

"""
This migration is named incorrectly.

We use it as a test for wrong autonames.
Please, do not rename it!
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Removes the default value from ``is_clean`` from ``SomeItem``."""

    dependencies = [
        ('main_app', '0003_update_is_clean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='someitem',
            name='is_clean',
            field=models.BooleanField(),
        ),
    ]
