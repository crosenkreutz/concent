# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 13:16
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160516_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
