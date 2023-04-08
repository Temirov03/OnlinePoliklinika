from django.contrib import admin

from .models import Sector,Hosptal

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name','app','add']
    search_fields = ['name']
    list_filter = ['app','add']

@admin.register(Hosptal)
class HosptalAdmin(admin.ModelAdmin):

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.MAHALLA.user_type == "sector_leader":
    #         queryset = queryset.filter (sector=queryset.MAHALLA.sector)
    #     return queryset

    list_display = ['name','sector']
    search_fields = ['name']
    list_filter = ['sector']