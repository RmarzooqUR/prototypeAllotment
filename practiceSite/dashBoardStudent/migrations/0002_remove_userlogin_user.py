# Generated by Django 2.1 on 2018-11-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoardStudent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogin',
            name='user',
        ),
    ]
