# Generated by Django 2.1.2 on 2019-06-17 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20190607_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='meta_title',
            new_name='description',
        ),
    ]
