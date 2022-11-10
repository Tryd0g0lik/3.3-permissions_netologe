from django.contrib import admin



# @admin.register(Advertisement)
from advertisements.models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
	list_display=('title', 'status', 'created_at', 'updated_at')
	list_filter=('id', 'status', 'created_at')

# admin.site.register(Advertisement, AdvertisementAdmin)
