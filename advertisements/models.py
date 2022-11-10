from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
# class AdvertisementStatusChoices():
    """Статусы объявления."""

#    choices = None
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""

    title = models.CharField(null=True, max_length=100)
    description = models.TextField(default='', max_length=300)
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
