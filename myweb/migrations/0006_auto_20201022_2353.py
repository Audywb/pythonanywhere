# Generated by Django 3.1.1 on 2020-10-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='notes',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='Phone_Number',
        ),
    ]
