# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        ('Profiler', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveIntegerField(choices=[(0, 'Book'), (1, 'Publication'), (2, 'Document'), (3, 'Web Links')])),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('name', models.CharField(max_length=50)),
                ('authors', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=20)),
                ('type', models.PositiveIntegerField(choices=[(0, 'Text Book'), (1, 'Reference Book')])),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('type', models.PositiveIntegerField(choices=[(0, 'Word Document'), (1, 'Text File'), (2, 'Presentation'), (3, 'PDF')])),
                ('source', models.URLField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publicationId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('title', models.CharField(max_length=150)),
                ('authors', models.CharField(max_length=70)),
                ('publicationDate', models.DateField()),
                ('organization', models.CharField(max_length=70)),
                ('webLink', models.URLField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('webLinkId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('link', models.URLField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='course',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Course'),
        ),
        migrations.AddField(
            model_name='resource',
            name='updatedBy',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Profiler.Faculty'),
        ),
    ]
