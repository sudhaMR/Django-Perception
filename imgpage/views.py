from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from imgpage.models import ImgObject,UserObject
import os
import json
from django.core.serializers.json import DjangoJSONEncoder
from perception.settings import STATIC_PATH
from os import listdir
from django.db.models import Count


def about(request):
    return HttpResponse("About page<a href='/imgpage/add_category.html'>Index</a>")

def request_title(path): #Path = C:/xyz/abc/a1.jpg
    flag=0
    s1,s2 = os.path.splitdrive(path)  #s1 = C: s2=/xyz/abc/a1.jpg
    s2,s3 = os.path.split(s2) #s3 = a1.jpg
    return str(s3)

def taginfo(request):
    #query_results = ImgObject.objects.all()
    a=[]
    query_results=[]
    for i in ImgObject.objects.values_list('img_title',flat=True).distinct():
              for j in ImgObject.objects.filter(img_title=str(i)).distinct().values_list('img_tags').annotate(the_count=Count('img_tags')):
                    k = "/static/images/"+i
                    (j1,j2)= j
                    print j1,j2
                    i1=i.replace('.jpg','')
                    i2=i1.replace('_',' ')
                    query_results.append([i2,j1,j2,k])

    for i in query_results:
        a.append(i)
    context = {'a': a}
    return render(request, 'imgpage/taginfo.html', context)

def imgArray(request):
    filepath = STATIC_PATH+"/images"
    imageArray=[]
    ext='.jpg'
    for i in os.listdir(filepath):
        if(os.path.splitext(i)[1] == ext):
             imageArray.append( i )
    json_list = json.dumps(list(imageArray), cls=DjangoJSONEncoder)
    return json_list


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        img_tags = request.POST.get('tags','')
        img_id = request.POST.get('id','')
        img_path = request.POST.get('filepath','')
        img_title = request_title(img_path)
        saving_tag = ImgObject(img_file = img_path,img_id=img_id, img_tags = img_tags,img_title = img_title)
        saving_tag.save()
                # If the request was not a POST, display the form to enter details.
        imageArray = imgArray(request)
        context = {'imageArray': imageArray}
        return render(request, 'imgpage/add_category.html',context)


    else:
        # If the request was not a POST, display the form to enter details.
        imageArray = imgArray(request)
        context = {'imageArray': imageArray}
        return render(request, 'imgpage/add_category.html',context)

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'imgpage/add_category.html')
