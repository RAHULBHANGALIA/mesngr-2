# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload', models.FileField(upload_to=b'uploads%Y%m%d')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='send_image_or_pdf',
            field=models.ForeignKey(blank=True, to='prjctapp.Upload', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_photo', models.FileField(upload_to=b'uploads%Y%m%d')),
                ('user_name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='message_to',
            field=models.ForeignKey(to='prjctapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='message_from',
            field=models.ForeignKey(to='prjctapp.User'),
            preserve_default=True,
        ),
    ]
