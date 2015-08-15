from django.db import models

class ImgObject(models.Model):
    img_file = models.CharField(max_length=128,unique=True)
    img_id = models.IntegerField(default=0)
    img_tags = models.CharField(max_length=320,unique=False)

    def __unicode__(self):
        return self.img_file

class UserObject(models.Model):
    user_id = models.IntegerField(default=0)
    user_email = models.EmailField(max_length=254)
    user_name = models.CharField(max_length=128,unique=False)

    def __unicode__(self):
        return self.user_id
    
    
# Create your models here.