# Generated by Django 4.0.4 on 2022-06-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0006_rename_categories_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.ManyToManyField(related_name='posts', to='app_api.topic'),
        ),
    ]
