# Generated by Django 2.2 on 2021-01-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210124_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.URLField(),
        ),
    ]
