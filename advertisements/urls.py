
from rest_framework.routers import DefaultRouter

from advertisements.views import AdvertisementViewSet

router = DefaultRouter()
router.register('advertising', AdvertisementViewSet)

urlpatterns = [

] + router.urls