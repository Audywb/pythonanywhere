# Generated by Django 3.1.1 on 2020-10-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0010_auto_20201025_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment2',
            name='N_slip',
            field=models.IntegerField(),
        ),
    ]
