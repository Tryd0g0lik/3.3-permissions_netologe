from django.contrib import admin

# Register your models here.
from advertisements.models import *

# admin.site.register(AdvertisementStatusChoices)


# @admin.register(AdvertisementStatusChoices)
# class AdvertisementStatusChoicesAdmin(admin.ModelAdmin):
# 	list_display=['status',]


# @admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
	list_display = ('title', )
	# list_filter=['id', 'status']
	# search_fields=('title', )
admin.site.register(Advertisement, AdvertisementAdmin)
