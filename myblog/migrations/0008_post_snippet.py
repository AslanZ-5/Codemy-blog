# Generated by Django 3.1.5 on 2021-02-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20210217_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read Blog Post... ', max_length=255),
        ),
    ]
