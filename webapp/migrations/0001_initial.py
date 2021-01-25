# Generated by Django 2.2 on 2021-01-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Под Заголовок')),
                ('description', models.CharField(max_length=3000, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('genre', models.CharField(max_length=255, verbose_name='Жанр')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('year', models.CharField(max_length=1000, verbose_name='Год выхода книги')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книгии',
            },
        ),
    ]
