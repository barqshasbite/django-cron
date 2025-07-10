# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_cron', '0004_alter_max_lengths'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='cronjoblog',
            new_name='django_cron_code_89ad04_idx',
            old_name='django_cron_cronjoblog_63e2740d',
        ),
        migrations.RenameIndex(
            model_name='cronjoblog',
            new_name='django_cron_code_21f381_idx',
            old_name='django_cron_cronjoblog_1fe0e40b',
        ),
        migrations.RenameIndex(
            model_name='cronjoblog',
            new_name='django_cron_code_966ed3_idx',
            old_name='django_cron_cronjoblog_495fb183',
        ),
    ]
