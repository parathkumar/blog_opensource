# Generated by Django 2.1.2 on 2019-07-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190709_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Display_Picture',
            field=models.ImageField(default='/pictures/pict.jpg', upload_to='pictures'),
        ),
    ]
