# Generated by Django 4.2.6 on 2025-01-22 14:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='intro',
            field=tinymce.models.HTMLField(verbose_name='内容'),
        ),
    ]
