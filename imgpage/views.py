from django.shortcuts import render
from django.http import HttpResponse
from imgpage.forms import ImgForm
from django.db import models
from imgpage.models import ImgObject,UserObject
import os
from perception.wsgi import file_dict,swap_dict

'''directory = 'C:\Users\MRSUDHA\Documents\GitHub\Django-Perception\static\images'
ext = '.jpg'
file_dict = {}
img_file_title = [i for i in os.listdir(directory) if os.path.splitext(i)[1] == ext]
c = 0

for i in os.listdir(directory):
    if(os.path.splitext(i)[1] == ext):
	    c=c+1
	    file_dict[i] = ["image"+ str(c)]
	    print i,c
		
#for f in img_file_title:
 #   file_dict[f]= "image"+str(c)
  #  c = c+1

for i in file_dict:
    print i,file_dict[i]

'''

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'imgpage/add_category.html', context_dict)
    #return HttpResponse("Enter words the picture reminds you of!<br/> <a href='/imgpage/about'>About</a> ")

def about(request):
    return HttpResponse("About page<a href='/imgpage/add_category.html'>Index</a>")


def request_title(path): #Path = C:/xyz/abc/a1.jpg
    s1,s2 = os.path.splitdrive(path)  #s1 = C: s2=/xyz/abc/a1.jpg
    s2,s3 = os.path.split(s2) #s3 = a1.jpg
    print "s3 "+s3
    for i in  swap_dict:
        print "i="+i
        print "swap "+swap_dict[i]
        if i == s3:
            return str(swap_dict[i])

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = ImgForm(request.POST)
        img_tags = request.POST.get('tags','')
        img_id = request.POST.get('id','')
        img_path = request.POST.get('filepath','')
        img_title = request_title(img_path)
        saving_tag = ImgObject(img_file = img_path,img_id=img_id, img_tags = img_tags,img_title = img_title)
        saving_tag.save()

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ImgForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'imgpage/add_category.html')
