# Generated by Django 3.1.1 on 2020-10-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0007_auto_20201023_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=10)),
                ('E_mail', models.CharField(max_length=100)),
                ('A_ddess', models.CharField(max_length=255)),
                ('P_code', models.CharField(max_length=10)),
                ('N_slip', models.CharField(max_length=10)),
            ],
        ),
    ]
