# Generated by Django 4.2.6 on 2025-01-21 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import forum.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=255, unique=True, verbose_name='分类名')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('cate_icon', models.FileField(upload_to=forum.models.cate_icon_path, verbose_name='图标')),
            ],
            options={
                'verbose_name': '帖子分类',
                'verbose_name_plural': '帖子分类',
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255, unique=True, verbose_name='标签名')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '帖子标签',
                'verbose_name_plural': '帖子标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='帖子标题')),
                ('content', tinymce.models.HTMLField(verbose_name='内容')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('post_order', models.IntegerField(default=0, verbose_name='排序')),
                ('lock', models.BooleanField(default=True, verbose_name='是否显示')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('thumb_up', models.PositiveIntegerField(default=0, verbose_name='点赞量')),
                ('thumb_down', models.PositiveIntegerField(default=0, verbose_name='点踩数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
                ('post_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.postcategory', verbose_name='所属模块')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_author', to=settings.AUTH_USER_MODEL, verbose_name='帖子作者')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_follower', to=settings.AUTH_USER_MODEL, verbose_name='关注者')),
            ],
        ),
    ]
