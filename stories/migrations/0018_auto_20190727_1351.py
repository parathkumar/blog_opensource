# Generated by Django 2.1.2 on 2019-07-27 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0017_auto_20190727_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
