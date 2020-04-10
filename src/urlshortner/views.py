from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .models import MyURL
from .forms import  SubmitURLForm


def  home_view_fbv(self,request,*args,**kwargs):
        if request.method == "POST":
                 print(request.POST)
        return render(request,"urlshortner/home.html",{})

class HomeView(View):
        def get(self,request,*args,**kwargs):
                the_form = SubmitURLForm()
                context = {
                        "title": "hawk.com",
                        "form": the_form
                }
                return render(request,"urlshortner/home.html",context)  

        def post(self,request,*args,**kwargs):
                form = SubmitURLForm(request.POST)
                context = {
                        "title": "hawk.com",
                        "form": form
                }
                template = "urlshortner/home.html"
                if form.is_valid():
                        new_url = form.cleaned_data.get("url")
                        obj, created = MyURL.objects.get_or_create(url=new_url )
                        context= {
                                "object":obj,
                                "created":created,
                        }
                        if created:
                                template = "urlshortner/success.html"
                        else:
                                template = "urlshortner/already-exists.html" 
                
                return render(request,template,context)                

class URLRediectView(View):  #it's a class base view to redirect
        def get(self, request,shortcode=None,*args,**kwargs):
                qs = MyURL.objects.filter(shortcode__iexact = shortcode)
                if qs.count() != 1 and not qs.exists():
                        raise Http404
                obj = qs.first()
                print(ClickEvent.objects.create_event(obj))
                return HttpResponseRedirect(obj.url)

   






'''
def My_redirect_view(request,shortcode=None,*args,**kwargs): #its a function ways to redirect
        #obj = MyURL.objects.get(shortcode=shortcode) it make does not exist if we just put any else shortcode
       # try:
       #     obj = MyURL.objects.get(shortcode=shortcode)
       # except:
       #     obj = MyURL.objects.al().first()   

        obj = get_object_or_404(MyURL,shortcode = shortcode)
        return HttpResponse("hello {sc}".format(sc = obj.url))

'''