from django.contrib import admin

# Register your models here.
from advertisements.models import AdvertisementStatusChoices, Advertisement


# @admin.register(AdvertisementStatusChoices)
# class AdvertisementStatusChoicesAdmin(admin.ModelAdmin):
# 	...



# @admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
	list_display=('title', 'status', 'created_at', 'updated_at')
	list_filter=('id', 'status', 'created_at')

admin.site.register(Advertisement, AdvertisementAdmin)
