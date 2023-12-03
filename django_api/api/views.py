from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.images import ImageFile
from . import models
from . import serializers
import ast
import matplotlib
import matplotlib.pyplot as plt
import io
matplotlib.use('agg')
def qualitative_compute(symptoms, scoring_weight, total_weight):
    
    results_qualitative = 0
    for i in range(len(symptoms)):
               results_qualitative = results_qualitative+ symptoms[i]*scoring_weight[i]
    results_qualitative = results_qualitative/total_weight
    return results_qualitative

# Create your views here
@api_view(["PUT"])
def set_ecg_value(request):
    """Function that sets the prediction value after the ECG analysis"""
    
    predict_value = models.PredictionValue.objects.get(pk=1)
    ser = serializers.PredictionValueSerializer(predict_value,data=request.data,partial=True)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
def get_ecg_value(request):
    pred = models.PredictionValue.objects.get(pk=1)
    return Response({"ecg_value":pred.ecg_value})


@api_view(["POST"])
def compute_total_value(request):
    """Function that compute the total prediction (qualitative + ml model)"""
    
    scoring_weight = [3,1,2,3,2,2,3]
    total_weight = sum(scoring_weight)
    symptoms = request.data.get("symptoms",[])

    symptoms = ast.literal_eval(symptoms)
    if symptoms ==[]:
         return Response({"Error":"No results were provided"},status=400)
    results_qualitative = qualitative_compute(symptoms, scoring_weight, total_weight)
    model_training = models.PredictionValue.objects.get(pk=1).ecg_value
    diagnostics = 0.7*model_training+ 0.3*results_qualitative*100

    predict_value = models.PredictionValue.objects.get(pk=1)
    predict_value.total_value = round(diagnostics,1)
    ser = serializers.PredictionValueSerializer(predict_value,data=request.data,partial=True)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    
    return Response(ser.errors)


@api_view(["GET"])
def get_total_value(request):
    """Function that compute the total prediction (qualitative + ml model)"""
    predictions = models.PredictionValue.objects.get(pk=1)
    return Response({"total_value":predictions.total_value})





@api_view(["POST"])
def create_ecg_plot(request):
    """Function that plot the ECG analyzed"""

    data = request.data.get("plot_vals",[])
    # data = ast.literal_eval(data)
    if data !=[]:

        figure = io.BytesIO()
        plt.axis("off")
    
        plt.plot(data,"#be2bbc")
        plt.savefig(figure, format="png")
        figure.seek(0)
        # Create an ImageFile object from the BytesIO object
        content_file = ImageFile(figure)
        # Update the ImageField of the model instance
        img = models.ImageEcg.objects.get(pk=1)
        img.image.save('ecg_plot.png', content_file)
        plt.close()
        return Response()
    return Response({"Error":"No data were provided"},status=400)

@api_view(["GET"])
def get_ecg_plot(request):
     
    img = models.ImageEcg.objects.get(pk=1)

    return Response({"url":img.image.url})
