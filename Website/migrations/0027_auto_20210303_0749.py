# Generated by Django 3.1.7 on 2021-03-03 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0026_auto_20210303_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevent',
            name='slug',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
