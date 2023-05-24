
from django.urls import path
from .views import *
from vehicle_selection import views


urlpatterns = [
    path('usedcar/', used_car),   
    path('search/',search_car),   #7 
    path('newcar/',new_cars),
    path('newcarfilter/',filter_list),  # 2,4
    path('preorder/',preorder),   #5
    path('displaycar/',display_cars),
    path('carprice/',displayfilter), #NEW CAR SEARCH  (1,3) 
    path('selectcar/',select_cars),
    path('aparna/',aparna_cars),  
    

]


#free input 8,9