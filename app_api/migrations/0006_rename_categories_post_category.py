# Generated by Django 4.0.4 on 2022-06-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0005_rename_category_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]
