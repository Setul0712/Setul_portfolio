# Generated by Django 2.2 on 2021-01-24 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201121_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
