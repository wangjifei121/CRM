# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-29 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180829_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish', verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishDate',
            field=models.DateField(auto_created=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
    ]
