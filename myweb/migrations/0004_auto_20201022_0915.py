# Generated by Django 2.2.7 on 2020-10-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20201022_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='number_slip',
            field=models.IntegerField(),
        ),
    ]