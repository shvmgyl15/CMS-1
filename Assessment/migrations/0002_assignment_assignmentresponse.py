# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0003_auto_20160418_1432'),
        ('Course', '0002_cirriculum'),
        ('Assessment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('deadline', models.DateField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('publishedDate', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseLink', models.URLField()),
                ('grade', models.CharField(max_length=1)),
                ('submissionDate', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
                ('student', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Profiler.Student')),
            ],
        ),
    ]
