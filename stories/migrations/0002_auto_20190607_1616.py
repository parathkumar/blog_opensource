# Generated by Django 2.1.2 on 2019-06-07 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='stories',
            name='picture',
            field=models.CharField(default='data:image/jpeg;base64,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', max_length=10000),
        ),
        migrations.AddField(
            model_name='rating',
            name='blog_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.stories'),
        ),
    ]
