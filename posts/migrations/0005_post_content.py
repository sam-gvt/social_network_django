# Generated by Django 5.0.2 on 2024-02-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='ok'),
            preserve_default=False,
        ),
    ]
