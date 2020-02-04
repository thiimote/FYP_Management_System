import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    start_date = DateFilter(field_name="date_posted", lookup_expr='gte')

    class Meta:
        model = FinalProject
        exclude = ['content', 'date_posted', 'introduction', 'problem_statement', 'scope', 'source_code']
        fields = '__all__'
