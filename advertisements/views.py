from django.http import HttpRequest
from django.shortcuts import render
from django_filters import DateFromToRangeFilter, FilterSet, DateTimeFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.widgets import RangeWidget
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer, AdvertisementFilterSerializer
from advertisements.permissions import OwnerPermissions


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, OwnerPermissions] # проверяем


class F(GenericViewSet, FilterSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementFilterSerializer
    created_at = DateFromToRangeFilter(field_name='created_at')
    print(created_at.__dict__)
    print(created_at.distinct)
    def date_filtrs(self, queryset, **kwargs):
        f = self.created_at
        after=Advertisement.objects.filter(created_at = kwargs[0])
        before=Advertisement.objects.filter(created_at = kwargs[1])

        # return queryset.filter(**{'after': kwargs[0], 'before': kwargs[1]})
        return {'after': after, 'before' : before}

    class Meta:
        model = Advertisement
        fields = ['created_at']
#
# print(f"F: {F}")
#

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров