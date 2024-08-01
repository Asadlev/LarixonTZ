from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Город'
    )

    def __str__(self):
        return self.name


class Advert(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    description = models.TextField()
    city = models.ForeignKey(
        City, on_delete=models.CASCADE,
        verbose_name='Категория города'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name='Категория обьявлений'
    )
    views = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.title
