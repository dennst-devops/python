# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-16 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAndRegAPP', '0003_user_bday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commentmaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_made', to='LoginAndRegAPP.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=2048)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messagemaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_made', to='LoginAndRegAPP.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='commenttomessage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_message', to='LoginAndRegAPP.Message'),
        ),
    ]