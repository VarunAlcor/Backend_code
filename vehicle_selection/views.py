
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from datetime import date, timedelta
from rest_framework.renderers import JSONRenderer

# Create your views here.

# @api_view(['GET'])
# def used_car(request):
#     uc = Usedcarstocks.objects.all()
#     serializer=Usedcarstocksserializer(uc, many=True)
#     return Response(serializer.data)




#GET & POST
@api_view(["GET","POST"])
def used_car(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            uc =  Usedcarstocks.objects.get(pk=id)
            serializer = Usedcarstocksserializer(uc)
            return Response(serializer.data)
        uc = Usedcarstocks.objects.all()
        serializer = Usedcarstocksserializer(uc, many = True)
        return Response(serializer.data)

    if request.methond == 'POST':
        serializer = Usedcarstocksserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)
#usedcar

@api_view(['GET'])
def search_car(request):
    queryset = Usedcarstocks.objects.all()
    serializer_class = Usedcarstocksserializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = Usedcarstocks_filter


    # Apply filter to queryset 

    filtered_queryset = filterset_class(
        data = request.query_params,
        queryset=queryset,
        request=request
    ).qs

    #apply search filter to queryset 

    search_term= request.query_params.get('search',None)
    starts_with_letter = request.query_params.get('starts_with', None)
    ends_with_letter = request.query_params.get('ends_with', None)

    if starts_with_letter is not None:
        filtered_queryset = filtered_queryset.filter(carname__istartswith=starts_with_letter)
    
    elif ends_with_letter is not None:
        filtered_queryset = filtered_queryset.filter(carname__iendswith=ends_with_letter)
    elif search_term is not None:
            filtered_queryset = filtered_queryset.filter(
                Q(modelyear__icontains=search_term) |
                Q(YOR__icontains=search_term) |
                Q(colorcode__icontains=search_term) |
                Q(expiredateofinsp__icontains=search_term) |
                Q(salesprice__icontains=search_term) |
                Q(bodyno__icontains=search_term) |
                Q(gradename__icontains=search_term) |
                Q(status__icontains=search_term) |
                Q(stockinventory__icontains=search_term)|
                Q(carname__icontains=search_term) |
                Q(mileage__icontains=search_term) 
        )

    # Serialize the filtered queryset
    serializer = serializer_class(filtered_queryset, many=True)
    return Response(serializer.data)



#NEW CAR LIST 
#get list of cars
@api_view(['GET'])
def new_cars(request):
    Newcarstock_obj=Newcarstock.objects.all() #queryset
    serializer=Newcarstockserializer(Newcarstock_obj, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def filter_list(request):
    queryset = Newcarstock.objects.all()
    serializer_class = Newcarstockserializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = Newcarstock_filter

    # Apply filters to the queryset
    filtered_queryset = filterset_class(
        data=request.query_params,
        queryset=queryset,
        request=request
    ).qs

    # Apply search filter to the queryset
    search_term = request.query_params.get('search', None)
    if search_term is not None:
        filtered_queryset = filtered_queryset.filter(
            Q(modelyear__icontains=search_term) |
            Q(modelcategory__icontains=search_term) |
            Q(grade__icontains=search_term) |
            Q(modelcode__icontains=search_term) |
            Q(commissionno__icontains=search_term) |
            Q(VINnumber__icontains=search_term) |
            Q(dealercode__icontains=search_term) |
            Q(modeltype__icontains=search_term) |
            Q(stockinventory__icontains=search_term)
        ) 

    # Serialize the filtered queryset
    serializer = serializer_class(filtered_queryset, many=True)
    return Response(serializer.data)

#PREORDER
# @api_view(['GET'])
# def preorder(request):
#     Preordercarstockmst_obj=Preordercarstockmst.objects.all() #queryset
#     serializer=Preordercarstockmstserializer(Preordercarstockmst_obj, many=True)
#     return Response(serializer.data)

def preorder(request):
    tomorrow = date.today() + timedelta(days=1)
    Preordercarstockmst_obj = Preordercarstockmst.objects.filter(applydateto__gte=tomorrow)
    serializer = Preordercarstockmstserializer(Preordercarstockmst_obj, many=True)
    response = Response(serializer.data)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = 'application/json'
    response.renderer_context = {'request': request}
    json_data = json.dumps(response.data)
    return HttpResponse(json_data, content_type='application/json')


#DISPLAY CAR 

@api_view(['GET'])
def display_cars(request):
    Displaycar_obj=Displaycar.objects.all() #queryset
    serializer=Displaycarserializer(Displaycar_obj, many=True)
    return Response(serializer.data)


#DISPLAY_FILTERING
@api_view(['GET'])
def displayfilter(request):
    queryset = Displaycar.objects.all()
    serializer_class = Displaycarserializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = Displaycar_filter

    # Apply filters to the queryset
    filtered_queryset = filterset_class(
        data=request.query_params,
        queryset=queryset,
        request=request
    ).qs

    # Apply search filter to the queryset
    search_term = request.query_params.get('search', None)
    if search_term is not None:
        filtered_queryset = filtered_queryset.filter(
            Q(modelyear__icontains=search_term) |
            Q(modelcategory__icontains=search_term) |
            Q(grade__icontains=search_term) |
            Q(modelcode__icontains=search_term) |
            Q(commissionno__icontains=search_term) |
            Q(VINnumber__icontains=search_term) |
            Q(dealercode__icontains=search_term) |
            Q(modeltype__icontains=search_term) |
            Q(stockinventory__icontains=search_term)
        ) 

    # Serialize the filtered queryset
    serializer = serializer_class(filtered_queryset, many=True)
    return Response(serializer.data)




#SELECT CARE  

@api_view(['GET'])
def select_cars(request):
    Selectedcar_obj=Selectedcar.objects.all() #queryset
    serializer=Selectedcarserializer(Selectedcar_obj, many=True)
    return Response(serializer.data)


#aparna
@api_view(['GET'])
def aparna_cars(request):
    aparna_obj=aparna.objects.all() #queryset
    serializer=aparnaserializer(aparna_obj, many=True)
    return Response(serializer.data)