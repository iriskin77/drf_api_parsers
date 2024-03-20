# Generated by Django 5.0 on 2024-03-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser_habr", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="author",
            field=models.CharField(max_length=255, verbose_name="Автор статьи"),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_link",
            field=models.URLField(max_length=10000, verbose_name="Ссылка на автора"),
        ),
        migrations.AlterField(
            model_name="texts",
            name="link",
            field=models.URLField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="texts",
            name="text",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="texts",
            name="title",
            field=models.CharField(max_length=10000, verbose_name="Заголовок"),
        ),
    ]