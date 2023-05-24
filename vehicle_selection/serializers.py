from rest_framework import serializers
from .models import *


class Usedcarstocksserializer(serializers.ModelSerializer):

    class Meta:
        model = Usedcarstocks
        fields = '__all__'

#New Car 

class Newcarstockserializer(serializers.ModelSerializer):

    class Meta:
        model=Newcarstock
        fields='__all__'

#PREORDER

class Preordercarstockmstserializer(serializers.ModelSerializer):

    class Meta:
        model=Preordercarstockmst
        fields='__all__'


#DISPLAYCAR

class Displaycarserializer(serializers.ModelSerializer):

    class Meta:
        model=Displaycar
        fields='__all__'

#SELECTED CARS 

class Selectedcarserializer(serializers.ModelSerializer):

    class Meta:
        model=Selectedcar
        fields='__all__'


#aparna


class aparnaserializer(serializers.ModelSerializer):

    class Meta:
        model=aparna
        fields='__all__'