from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Título",
    )
    author = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default="Desconhecido",
        verbose_name="Autor",
    )
    year = models.IntegerField(
        validators=[MaxValueValidator(2024)],
        blank=True,
        null=True,
        verbose_name="Ano de lançamento",
    )
    page_numbers = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Número de páginas",
    )
    read = models.BooleanField(
        default=False,
        verbose_name="Lido?",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["id"]
