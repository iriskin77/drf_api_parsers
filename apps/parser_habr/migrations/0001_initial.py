# Generated by Django 5.0 on 2024-01-01 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.CharField(max_length=255, verbose_name="Автор статьи"),
                ),
                (
                    "author_link",
                    models.URLField(max_length=10000, verbose_name="Ссылка на автора"),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "celery_task_id",
                    models.CharField(max_length=1001, verbose_name="id celery"),
                ),
                (
                    "is_success",
                    models.BooleanField(default=False, verbose_name="Статус задачи"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Задачи",
                "verbose_name_plural": "Задачи",
            },
        ),
        migrations.CreateModel(
            name="Timer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("minutes", models.IntegerField()),
            ],
            options={
                "verbose_name": "Период обхода хабов",
                "verbose_name_plural": "Период обхода хабов",
            },
        ),
        migrations.CreateModel(
            name="Hub",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hub_name",
                    models.CharField(max_length=255, verbose_name="Название хаба"),
                ),
                (
                    "hub_link",
                    models.URLField(max_length=10000, verbose_name="Ссылка на хаб"),
                ),
                (
                    "task_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="parser_habr.task",
                    ),
                ),
            ],
            options={
                "verbose_name": "Хабы",
                "verbose_name_plural": "Хабы",
            },
        ),
        migrations.CreateModel(
            name="Texts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=10000, verbose_name="Заголовок")),
                ("text", models.TextField()),
                (
                    "date",
                    models.CharField(
                        max_length=255, verbose_name="Дата публикации на Habr"
                    ),
                ),
                ("link", models.URLField(max_length=10000)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="parser_habr.author",
                        verbose_name="Автор статьи",
                    ),
                ),
                (
                    "hub",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="parser_habr.hub",
                        verbose_name="Название хаба",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]
