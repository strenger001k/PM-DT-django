from django.contrib import admin
from firstapp.models import Сategory, Product
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


@admin.register(Product)
class StateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'card',)


admin.site.register(Сategory, MPTTModelAdmin)
