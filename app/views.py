from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_topics(request):
    topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='Cricket')
    topics=Topic.objects.exclude(topic_name='Cricket')
    d={'topics':topics}
    return render(request, 'display_topics.html',d)


def display_webpages(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='Cricket')
    webpages=Webpage.objects.exclude(topic_name='Cricket')
    webpages=Webpage.objects.all()[:3:]
    webpages=Webpage.objects.all()[::-1]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name__startswith='H')
    webpages=Webpage.objects.filter(name__endswith='i')
    webpages=Webpage.objects.filter(name__contains='h')
    webpages=Webpage.objects.filter(Q(name='sri') | Q(url='https'))
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Virat') | Q(url='https'))
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)



def display_accessrecords(request):
    accessrecords=AccessRecord.objects.all()
    accessrecords=AccessRecord.objects.filter(date='2000-05-22')
    accessrecords=AccessRecord.objects.filter(date__year='2000')
    accessrecords=AccessRecord.objects.filter(date__year__gt='2000')
    accessrecords=AccessRecord.objects.filter(date__year__gte='2000')
    accessrecords=AccessRecord.objects.filter(date__year__lt='2000')
    accessrecords=AccessRecord.objects.filter(date__year__lte='2000')

    
    
    


    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)





