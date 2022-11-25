
from django_filters import DateFromToRangeFilter, FilterSet, DateTimeFilter, DateTimeFromToRangeFilter, CharFilter
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


class F2(GenericViewSet, FilterSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementFilterSerializer
    created_at = DateFromToRangeFilter(field_name='created_at')

    def date_filtrs(self, queryset, **kwargs):
        f = self.created_at
        after=Advertisement.objects.filter(created_at = kwargs[0])
        before=Advertisement.objects.filter(created_at = kwargs[1])
        return {'after': after, 'before' : before}

    class Meta:
        model = Advertisement
        fields = ['created_at']

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

class dataFilterSet(FilterSet):

    created_at = DateTimeFromToRangeFilter()
    status = CharFilter()
    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']


class FListCreateAPIView(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementFilterSerializer
    filterset_class = dataFilterSet
