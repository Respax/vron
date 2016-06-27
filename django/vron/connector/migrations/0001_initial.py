# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=100, verbose_name=b'option name')),
                ('value', models.CharField(max_length=100, verbose_name=b'option value')),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_config', 'ADMIN: Can add config option'), ('admin_change_config', 'ADMIN: Can change config option'), ('admin_delete_config', 'ADMIN: Can delete config option'), ('admin_view_config', 'ADMIN: Can view config options')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=20, verbose_name=b'name')),
                ('comments', models.CharField(max_length=255, null=True, verbose_name=b'comments', blank=True)),
                ('payment_option', models.CharField(max_length=255, null=True, verbose_name=b'Payment option', blank=True)),
                ('last_update_payment', models.DateTimeField(null=True, blank=True)),
                ('clear_payment_option', models.NullBooleanField(default=False)),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_add_config', 'ADMIN: Can add config option'), ('admin_change_config', 'ADMIN: Can change config option'), ('admin_delete_config', 'ADMIN: Can delete config option'), ('admin_view_config', 'ADMIN: Can view config options')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('external_reference', models.CharField(max_length=40, null=True, verbose_name=b'external reference', blank=True)),
                ('error_message', models.TextField(null=True, verbose_name=b'error message', blank=True)),
                ('ron_confirmation_number', models.IntegerField(null=True, verbose_name=b'confirmation number', blank=True)),
                ('attempts', models.IntegerField(default=1, verbose_name=b'attempts')),
            ],
            options={
                'default_permissions': [],
                'permissions': (('admin_view_request', 'ADMIN: Can view logs'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified date')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='log',
            name='log_status',
            field=models.ForeignKey(to='connector.LogStatus'),
            preserve_default=True,
        ),
    ]
