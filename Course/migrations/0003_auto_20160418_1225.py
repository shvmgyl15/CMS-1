# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0003_auto_20160418_1432'),
        ('Course', '0002_cirriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegroup',
            name='instructor',
            field=models.ForeignKey(to='Profiler.Faculty', default='None'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(to='Profiler.Faculty', default=False, related_name='head_of_dept'),
        ),
    ]
