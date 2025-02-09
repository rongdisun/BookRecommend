# Generated by Django 4.2.6 on 2025-01-21 13:21

import article.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('cover', models.FileField(max_length=255, upload_to=article.models.article_cover_path, verbose_name='封面')),
                ('summary', models.CharField(max_length=255, verbose_name='摘要')),
                ('content', tinymce.models.HTMLField(verbose_name='内容')),
                ('post_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('article_views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('article_order', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.SmallIntegerField(default=1, verbose_name='发布状态')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_category', to='article.category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='article_tag', to='article.tag', verbose_name='标签集合')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
                'ordering': ['-article_order', '-post_time'],
            },
        ),
    ]
