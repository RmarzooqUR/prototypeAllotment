# Generated by Django 2.1 on 2018-11-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoardProvost', '0005_roommodel_seater'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='vacant',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
