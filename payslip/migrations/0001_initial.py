# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 10:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='HR number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('title', models.CharField(choices=[(b'1', b'Ms.'), (b'2', b'Mrs.'), (b'3', b'Mr.'), (b'4', b'Dr.')], max_length=1, verbose_name='Title')),
                ('is_manager', models.BooleanField(default=False, verbose_name='is Manager')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='payslip.Company', verbose_name='Company')),
            ],
            options={
                'ordering': ['company__name', 'user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='ExtraField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
            ],
            options={
                'ordering': ['field_type__name'],
            },
        ),
        migrations.CreateModel(
            name='ExtraFieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('model', models.CharField(blank=True, choices=[(b'Employee', b'Employee'), (b'Payment', b'Payment'), (b'Company', b'Company')], max_length=10, null=True, verbose_name='Model')),
                ('fixed_values', models.BooleanField(default=False, verbose_name='Fixed values')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 4, 29, 5, 51, 42, 30178), verbose_name='Date')),
                ('end_date', models.DateTimeField(blank=True, help_text='This field is only considered, if the payment type has a recurring rule.', null=True, verbose_name='End of recurring period')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payslip.Employee', verbose_name='Employee')),
                ('extra_fields', models.ManyToManyField(blank=True, null=True, to='payslip.ExtraField', verbose_name='Extra fields')),
            ],
            options={
                'ordering': ['employee__user__first_name', '-date'],
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('rrule', models.CharField(blank=True, choices=[(b'MONTHLY', 'Monthly'), (b'YEARLY', 'Yearly')], max_length=10, verbose_name='Recurring rule')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payslip.PaymentType', verbose_name='Payment type'),
        ),
        migrations.AddField(
            model_name='extrafield',
            name='field_type',
            field=models.ForeignKey(help_text='Only field types with fixed values can be chosen to add global values.', on_delete=django.db.models.deletion.CASCADE, related_name='extra_fields', to='payslip.ExtraFieldType', verbose_name='Field type'),
        ),
        migrations.AddField(
            model_name='employee',
            name='extra_fields',
            field=models.ManyToManyField(blank=True, null=True, to='payslip.ExtraField', verbose_name='Extra fields'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='company',
            name='extra_fields',
            field=models.ManyToManyField(blank=True, null=True, to='payslip.ExtraField', verbose_name='Extra fields'),
        ),
    ]
