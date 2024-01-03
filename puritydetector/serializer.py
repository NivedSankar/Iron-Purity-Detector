from rest_framework import serializers 
from .models import MLModelData 

class IronPuritySerializers(serializers.ModelSerializer): 
    class meta: 
        model=MLModelData 
        fields='__all__'