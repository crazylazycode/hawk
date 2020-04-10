from django.db import models

from urlshortner.models import MyURL 
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, MyInstance):
        if isinstance(MyInstance,  MyURL):
            obj, created = self.get_or_create(my_url = MyInstance )
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    my_url    =  models.OneToOneField(MyURL, on_delete=models.CASCADE)
    count     =  models.IntegerField(default=0)
    updated   =  models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp =  models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
