# Generated by Django 3.1.7 on 2021-03-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0029_auto_20210303_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevent',
            name='slug',
            field=models.SlugField(default=True, primary_key=True, serialize=False),
        ),
    ]
