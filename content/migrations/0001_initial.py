# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 13:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textAnswer', models.CharField(max_length=100, verbose_name='Ответ')),
                ('valueAnswer', models.SmallIntegerField(blank=True, default=0, verbose_name='количество ответов')),
                ('persent', models.SmallIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'db_table': 'faq',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateField(auto_now_add=True, verbose_name='Время создания')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок новости')),
                ('textNews', ckeditor.fields.RichTextField(verbose_name='Текст Новости')),
                ('imgNews', models.ImageField(blank=True, default='images/noimage.jpg', null=True, upload_to='static/media/images/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textQuestion', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('dateQuestion', models.DateField(auto_now_add=True, verbose_name='Дата создания вопроса')),
                ('usersAnswers', models.SmallIntegerField(blank=True, default=0, verbose_name='Количество проголосовавших')),
                ('is_active', models.BooleanField(verbose_name='Активный опрос')),
            ],
            options={
                'verbose_name': 'Голосование',
                'verbose_name_plural': 'Голосование',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('rating', models.SmallIntegerField(verbose_name='Рейтинг')),
                ('comment', models.TextField(verbose_name='Отзыв')),
                ('dateCreate', models.DateField(auto_now_add=True, verbose_name='Дата создания отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'testimonials',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Question', verbose_name='Относится к вопросу'),
        ),
    ]
