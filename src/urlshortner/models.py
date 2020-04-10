from django.db import models

from django.conf import settings
from django_hosts.resolvers import reverse


from .utils import code_generator,create_shortcode
from .validators import validate_url,validate_dot_com


SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",25)

class MyURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main = super(MyURLManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self,items=None):
        qs = MyURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)    




class MyURL(models.Model):
    url = models.CharField(max_length=220,validators=[validate_url,validate_dot_com])
    shortcode = models.CharField(max_length = SHORTCODE_MAX, unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False,auto_now_add=False) 
    #shortcode = models.CharField(max_length=25, null=True) Empty in database is okay
    #shortcode = models.CharField(max_length=25, default='admindefaultshortcode')
    
    objects = MyURLManager()


    #some_random = MyURLManager() it does similar to mai django manager it same cause it refernce it
    
    
    
    def __str__(self):
        return str(self.url)

    def __unicode__(self): 
        return str(self.url)

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(MyURL,self).save(*args,**kwargs)

    #def my_save(self):
       # super(MyURL,self).save(*args,**kwargs)    

    def get_short_url(self):
        url_path = reverse("scode",kwargs={'shortcode' : self.shortcode},host='www',scheme='http')
        return  url_path

'''
to run any change we need to run two command an then run the server
1, python manage,py makemigrations
2. python manage.py migrate 
and the run the server by using command
python manage.py runserver
'''