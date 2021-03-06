from django.shortcuts import render
from .models import *
import django_filters
from rest_framework import viewsets, filters
from .serializer import *
# Create your views here.
import datetime

def nowlog(request):
    model = PdaChatLog.objects.all().order_by('-date_time')[0:30]
    if request.method == 'GET':
        model = PdaChatLog.objects.all().order_by('-date_time')[0:30]

    d = datetime.timedelta(hours=8)
    return render(request,'rialtime.html',{
        'model' : model,
        'd' : d
    })


class ChatViewSet(viewsets.ModelViewSet):
    queryset = PdaChatLog.objects.all().order_by('-date_time')[0:100]
    serializer_class = ChatSerializer