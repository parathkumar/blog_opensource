# Generated by Django 2.1.2 on 2019-07-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0015_auto_20190722_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='picture',
            field=models.ImageField(default='/pictures/pict.jpg', upload_to='pictures/'),
        ),
    ]