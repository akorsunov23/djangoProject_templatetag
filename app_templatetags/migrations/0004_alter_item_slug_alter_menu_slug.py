# Generated by Django 4.1.7 on 2023-02-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_templatetags', '0003_alter_item_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]