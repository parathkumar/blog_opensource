# Generated by Django 2.1.2 on 2019-07-27 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_auto_20190725_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
    ]
