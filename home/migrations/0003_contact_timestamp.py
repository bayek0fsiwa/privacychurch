# Generated by Django 2.2.12 on 2020-04-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200411_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]