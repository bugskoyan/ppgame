import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Game
        fields = ['name']

