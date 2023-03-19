from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import utils
from django.conf import settings

#@api_view(['GET'])
def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def tutorial_page(request):
    template = loader.get_template('tutorial.html')
    return HttpResponse(template.render())

def preview_page(request, file_name):
    context = {
        'path': settings.MEDIA_URL + file_name,
        'preview_route': settings.PREVIEW_ROUTE + file_name
    }
    return render(request, 'preview.html', context)

@api_view(['POST'])
def uploadFile(request):
    try:
        file = request.FILES['file']
        jsonFile = utils.parseJson(file)
        data_string = utils.findMessages(jsonFile)
        image_url = utils.createWordcloud(data_string, data=request.data)
        return redirect(settings.PREVIEW_ROUTE + image_url)
    except:
        return redirect('/')