# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cron', '0003_cronjoblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjoblock',
            name='job_name',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='cronjoblog',
            name='code',
            field=models.CharField(db_index=True, max_length=1000),
        ),
    ]
