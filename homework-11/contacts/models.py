from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="Ім'я"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Прізвище"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone = models.CharField(
        max_length=30,
        verbose_name="Контактний телефон"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Примітки"
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"