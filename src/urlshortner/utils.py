import random
import string

from django.conf import settings
SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)

#from urlshortner.models import MyURL is gives error cause both file are asking from data to each other with cant be done

# Create your models here.
def code_generator(size=SHORTCODE_MIN,chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
   # new_code = ''
     #for _ in range(size):
    #   new_code +=random.choice(chars)
    #return new_code
    return ''.join(random.choice(chars)for i in range(size))

def create_shortcode(instance ,size=SHORTCODE_MIN):
  new_code = code_generator(size=size)
  klass = instance.__class__
  qs_exists = klass.objects.filter(shortcode=new_code)
  if qs_exists:
    return create_shortcode(size=size)
  return new_code