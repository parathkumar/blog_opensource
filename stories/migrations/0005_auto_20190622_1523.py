# Generated by Django 2.1.2 on 2019-06-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20190617_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='content',
            field=models.CharField(max_length=100000),
        ),
    ]
