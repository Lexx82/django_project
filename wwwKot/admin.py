from django.contrib import admin

# Register your models here.
from .models import *


class WwwTblAdmin(admin.ModelAdmin):
    list_display = ('dep', 'hw_info', 'url', 'note')
    list_display_links = ('hw_info', 'url')
    search_fields = ('dep', 'hw_info')


class DepTblAdmin(admin.ModelAdmin):
    list_display = ('id', 'dep')
    list_display_links = ('dep',)


class HwTblAdmin(admin.ModelAdmin):
    list_display = ('id', 'hw_info')
    list_display_links = ('hw_info',)


admin.site.register(WwwTbl, WwwTblAdmin)
admin.site.register(DepTbl, DepTblAdmin)
admin.site.register(HwTbl, HwTblAdmin)