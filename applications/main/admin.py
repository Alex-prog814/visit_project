from django.contrib import admin

from applications.main.models import Worker, TradePoint, Visit


class WorkerAdminDisplay(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name', )


class TradePointAdminDisplay(admin.ModelAdmin):
    list_display = ('title', 'worker')
    search_fields = ('title', )


class VisitAdminDisplay(admin.ModelAdmin):
    list_display = ('trade_point', 'get_worker', 'latitude', 'longitude', 'date')
    search_fields = ('trade_point__title', 'trade_point__worker__name')

    def get_worker(self, obj):
        return obj.trade_point.worker.name


admin.site.register(Worker, WorkerAdminDisplay)
admin.site.register(TradePoint, TradePointAdminDisplay)
admin.site.register(Visit, VisitAdminDisplay)
