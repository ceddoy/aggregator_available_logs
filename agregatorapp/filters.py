import datetime

from django_filters.rest_framework import FilterSet, filters, RangeFilter, DateFromToRangeFilter
from django_filters.fields import DateRangeField

from agregatorapp.models import Log


class CustomDateRangeField(DateRangeField):
    def compress(self, data_list):
        if data_list:
            start_date, stop_date = data_list
            if start_date and not stop_date:
                stop_date = datetime.datetime.max
            elif not start_date and stop_date:
                start_date = datetime.datetime.min
                stop_date += datetime.timedelta(days=1)
            else:
                stop_date += datetime.timedelta(days=1)
            return start_date, stop_date
        return None


class CustomDateFromToRangeFilter(RangeFilter):
    field_class = CustomDateRangeField


class LogsFilter(FilterSet):

    ip_address = filters.CharFilter(lookup_expr='exact')
    date_add = filters.DateFilter(lookup_expr='contains')
    date_range = CustomDateFromToRangeFilter(lookup_expr='contains', method='date_range_filter')

    class Meta:
        model = Log
        fields = ['ip_address', 'date_add', 'date_range']

    def date_range_filter(self, queryset, name, value):
        return queryset.filter(date_add__range=value)
