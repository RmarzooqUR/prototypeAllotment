# Generated by Django 2.1 on 2018-11-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashBoardProvost', '0004_auto_20181112_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='seater',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
