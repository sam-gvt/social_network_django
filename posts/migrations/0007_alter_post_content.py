# Generated by Django 5.0.2 on 2024-02-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_chatpost_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=50000),
        ),
    ]
