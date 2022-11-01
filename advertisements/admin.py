from django.contrib import admin

# Register your models here.
from advertisements.models import AdvertisementStatusChoices, Advertisement

admin.site.register(AdvertisementStatusChoices)
admin.site.register(Advertisement)

# @admin.register(AdvertisementStatusChoices)
# class AdvertisementStatusChoicesAdmin(admin.ModelAdmin):
# 	list_display=['status',]

# @admin.register(Advertisement)
# class AdvertisementAdmin(admin.ModelAdmin):
# 	list_display=['title', 'status', 'creator', 'created_at', 'updated_at']
# 	list_filter=['id', 'status']
# 	search_fileds=('title', )