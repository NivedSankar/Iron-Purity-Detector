from .forms import IronForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import MLModelData 
from .serializer import IronPuritySerializers 


import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()

class IronPurityView(viewsets.ModelViewSet): 
    queryset = MLModelData.objects.all() 
    serializer_class = IronPuritySerializers 

def predict_result(df):
    try:
        scaler=pickle.load(open("Ml data/scaler.sav", 'rb'))
        model=pickle.load(open("Ml data/sgd_model.sav", 'rb'))
        
        pred = model.predict(scaler.transform(df)) 
        print(pred)
        result = f"Good Quality Iron \n {pred}" if pred<=3 else f"Bad Quality Iron \n {pred}"
        return result
    except ValueError as e: 
        raise e

def FormView(request):
    if request.method=='POST':
        form=IronForm(request.POST or None)

        if form.is_valid():
            form.save()
            iron_feed = form.cleaned_data['iron_feed']
            silica_feed = form.cleaned_data['silica_feed']
            starch_flow = form.cleaned_data['starch_flow']
            
            amina_flow = form.cleaned_data['amina_flow']
            ore_pulp_flow = form.cleaned_data['ore_pulp_flow']
            ore_pulp_density = form.cleaned_data['ore_pulp_density']
            
            column_04_air_flow = form.cleaned_data['column_04_air_flow']
            column_05_air_flow = form.cleaned_data['column_05_air_flow']
            column_06_air_flow = form.cleaned_data['column_06_air_flow']
            column_07_air_flow = form.cleaned_data['column_07_air_flow']
            
            column_01_level = form.cleaned_data['column_01_level']
            column_02_level = form.cleaned_data['column_02_level']
            column_03_level = form.cleaned_data['column_03_level']
            column_04_level = form.cleaned_data['column_04_level']
            column_05_level = form.cleaned_data['column_05_level']
            column_06_level = form.cleaned_data['column_06_level']
            column_07_level = form.cleaned_data['column_07_level']
            
            
            data = {
                '% Iron Feed': [iron_feed],
                '% Silica Feed': [silica_feed],
                'Starch Flow': [starch_flow],
                'Amina Flow': [amina_flow],
                'Ore Pulp Flow': [ore_pulp_flow],
                'Ore Pulp Density': [ore_pulp_density],
                'Flotation Column 04 Air Flow' : [column_04_air_flow],
                'Flotation Column 05 Air Flow' : [column_05_air_flow],
                'Flotation Column 06 Air Flow' : [column_06_air_flow],
                'Flotation Column 07 Air Flow' : [column_07_air_flow],
                'Flotation Column 01 Level' : [column_01_level],
                'Flotation Column 02 Level' : [column_02_level],
                'Flotation Column 03 Level' : [column_03_level],
                'Flotation Column 04 Level' : [column_04_level],
                'Flotation Column 05 Level' : [column_05_level],
                'Flotation Column 06 Level' : [column_06_level],
                'Flotation Column 07 Level' : [column_07_level],
            }
            df=pd.DataFrame(data)
            try:
                result = predict_result(df)  # Call the predict_result function
                return render(request, 'result.html', {"data": result,'df':df})
            except ValueError as e:
                error_message = str(e)
                return JsonResponse({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
    form=IronForm()
    return render(request, 'user_input.html', {'form':form})