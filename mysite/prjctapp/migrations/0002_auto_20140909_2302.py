# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prjctapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.FileField(null=True, upload_to=b'uploads%Y%m%d', blank=True),
        ),
    ]
