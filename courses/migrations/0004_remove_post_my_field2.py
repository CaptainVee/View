# Generated by Django 3.1.2 on 2021-02-09 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='my_field2',
        ),
    ]
