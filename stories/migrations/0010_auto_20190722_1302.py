# Generated by Django 2.1.2 on 2019-07-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_auto_20190722_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='author',
            field=models.CharField(default='guest', max_length=100),
        ),
    ]
