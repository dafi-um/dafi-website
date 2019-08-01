from django.contrib import admin

from .models import TradePeriod, TradeOffer


class TradePeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')


class TradeOfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date')
    list_filter = ['user', 'pub_date']


admin.site.register(TradePeriod, TradePeriodAdmin)
admin.site.register(TradeOffer, TradeOfferAdmin)