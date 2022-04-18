from pydoc_data.topics import topics
from django.shortcuts import render
from app.models import *
# Create your views 
def display_topic(request):
    topics=Topic.objects.all(
    d={'ts':topics}
    return render(request,'display_topic',d)
    


def display_webpage(request):
    #webpages=webpage.objects.all()
    #webpages=webpage.objects.filter(topic_name='Foot Ball')
    webpages=webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}r')
    
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)

def display_access(request):
    #access=AccessRecords.objects.all()
    #access=AccessRecords.objects.filter(date='1990_03_30')
    access=AccessRecords.objects.filter(date__gte='1990_03_30')
    acess=Aceeesrecords.objects.filter(date__gte='1990')
    acess=AcessRecords.objects.filter(date__year='2000')
    access=AccessRecor.object
    d={'ac':access}
    return render(request,'display_access.html',d)