# Generated by Django 3.1.1 on 2020-10-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0013_auto_20201025_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment2',
            name='A_ddess',
            field=models.TextField(blank=True),
        ),
    ]
