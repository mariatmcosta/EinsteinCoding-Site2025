from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Título"
    )

    summary = models.TextField(
        max_length=500,
        verbose_name="Resumo"
    )

    content = models.TextField(
        verbose_name="Conteúdo completo"
    )

    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True,
        verbose_name="Imagem da notícia"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Destaque na Home"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última atualização"
    )

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
