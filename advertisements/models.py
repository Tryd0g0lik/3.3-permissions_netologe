from django.conf import settings
from django.db import models


# class AdvertisementStatusChoices(models.TextChoices):
#     """Статусы объявления."""
#
#     OPEN = "OPEN", "Открыто"
#     CLOSED = "CLOSED", "Закрыто"

class AdvertisementStatusChoices(models.Model):
    """Статусы объявления."""
    STATUS=(
        ('OPEN', 'OPEN/Открыто'),
        ('CLOSED', 'CLOSED/Закрыто'),
    )
    status = models.CharField(max_length=1,
                              choices=STATUS,
                              default='OPEN',
                              )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    # status = models.TextField(
    #     choices=AdvertisementStatusChoices.choices,
    #     default=AdvertisementStatusChoices.OPEN
    # )
    status = models.ForeignKey(AdvertisementStatusChoices,
                               on_delete=models.CASCADE,
                               verbose_name='Статус',)
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
