# Generated by Django 2.1.3 on 2018-11-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_authordetall_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetall',
            name='phone',
            field=models.IntegerField(default=155),
            preserve_default=False,
        ),
    ]
