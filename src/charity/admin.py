import datetime

from django.contrib import admin
from django.db.models import F
from . import models


class CharityDateFilter(admin.SimpleListFilter):
    title = 'Период сбора средств'
    parameter_name = 'date_status'
    
    def lookups(self, request, model_admin):
        return(
            ('active', 'Сбор продолжается'),
            ('completed', 'Сбор завершён'),
        )

    def queryset(self, request, queryset):                    
        today = datetime.date.today()
        if self.value() == 'active':
            queryset = queryset.filter(ending__gte=today).distinct()
        if self.value() == 'completed':
            queryset = queryset.filter(ending__lt=today).distinct()
        return queryset
    
    
class CharityAmountFilter(admin.SimpleListFilter):
    title = 'Собранное количество средств'
    parameter_name = 'amount_status'
    
    def lookups(self, request, model_admin):
        return(
            ('active', 'Сумма не собрана'),
            ('completed', 'Сумма собрана'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'active':
            queryset = queryset.filter(amount__lt=F('final_amount')).distinct()
        if self.value() == 'completed':
            queryset = queryset.filter(amount__gte=F('final_amount')).distinct()
        return queryset
        

class CharityPhotoInline(admin.TabularInline):
    model = models.CharityPhoto
    extra = 0
    
    
@admin.register(models.Charity)
class CharityAdmin(admin.ModelAdmin):
    inlines = (CharityPhotoInline,)
    list_display = ('surname', 'name', 'starting',
                    'ending', 'amount', 'final_amount',
                    'display')
    search_fields = ('surname', 'diagnosis')
    list_filter = ('display', CharityDateFilter, CharityAmountFilter)

