"""
WSGI config for perception project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "perception.settings")


directory = 'C:\Users\MRSUDHA\Documents\GitHub\Django-Perception\static\images'
ext = '.jpg'
file_dict = {}
swap_dict = {}
img_file_title = [i for i in os.listdir(directory) if os.path.splitext(i)[1] == ext]
c = 0

for i in os.listdir(directory):
    if(os.path.splitext(i)[1] == ext):	    
	    file_dict[i] = ("image"+ str(c)+".jpg")	   
	    c=c+1
		

'''for i in file_dict:
    print i,file_dict[i]'''
print "File dict"
print file_dict

for key, val in file_dict.items():
        swap_dict[val] = key
print "File dict"
print swap_dict
        
for key,val in file_dict.items():
	os.rename(directory+'//'+key,directory+'//'+val)


application = get_wsgi_application()
