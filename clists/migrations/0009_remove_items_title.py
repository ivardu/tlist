# Generated by Django 2.2 on 2020-05-26 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clists', '0008_auto_20200526_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='title',
        ),
    ]
