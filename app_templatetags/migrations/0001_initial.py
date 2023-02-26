# Generated by Django 4.1.7 on 2023-02-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='позиция')),
                ('slug', models.SlugField()),
            ],
        ),
    ]
