# Generated by Django 2.2.13 on 2020-07-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200726_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
