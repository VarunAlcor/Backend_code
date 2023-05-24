from rest_framework .filters import SearchFilter
from vehicle_selection.models import *
from django_filters import filters
from django_filters import rest_framework as filters


class Usedcarstocks_filter(filters.FilterSet):
    class Meta:
        model = Usedcarstocks
        fields = ('__all__')



class Newcarstock_filter(filters.FilterSet):
    class Meta:
        model = Newcarstock
        fields = ('__all__')



class Displaycar_filter(filters.FilterSet):
    class Meta:
        model = Displaycar
        fields = ('__all__')