# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-01 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputbox', '0003_remove_article_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sample_cover',
            field=models.FileField(upload_to=b''),
        ),
    ]
