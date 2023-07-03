from .models import Order
from django_filters import FilterSet, DateRangeFilter


class OrderFilter(FilterSet):
    start_date = DateRangeFilter(field_name='date_created',lookup_expr='gte')
    end_date = DateRangeFilter(field_name='date_created',lookup_expr='lte')
    class Meta:
        model = Order
        fields ='__all__'
        exclude = ['customer','date_created']