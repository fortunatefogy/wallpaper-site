
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import os

from django.views.generic import DetailView

from .views import *
from .forms import *
from .models import *
from django.core.mail import send_mail
# from food.settings import EMAIL_HOST_USER
import uuid
from django.contrib import messages
from django.contrib.auth import authenticate

from .forms import *

# Create your views here.
def main(request):
    return render(request,"index.html")

def wallupload(request):
    if request.method == 'POST':
        a=walluploadform(request.POST, request.FILES)
        if a.is_valid():
            im=a.cleaned_data['image']
            ca=a.cleaned_data['category']
            imn=a.cleaned_data['imagename']
            if ca=="amoled":
                am=amoleds(image=im,imagename=imn,category=ca)
                am.save()
                return redirect(amoleddisplay)
            elif ca=="dark":
                da=darks(image=im,imagename=imn,category=ca)
                da.save()
                return redirect(darkdisplay)
            elif ca=="abstract":
                ab=abstracts(image=im,imagename=imn,category=ca)
                ab.save()
                return redirect(abstractdisplay)
            elif ca=="movies":
                mo=moviess(image=im,imagename=imn,category=ca)
                mo.save()
                return redirect(moviesdisplay)
            elif ca=="girl":
                gi=girls(image=im,imagename=imn,category=ca)
                gi.save()
                return redirect(girldisplay)

            elif ca=="nature":
                na=natures(image=im,imagename=imn,category=ca)
                na.save()
                return redirect(naturedisplay)
            elif ca=="animals":
                an=animals(image=im,imagename=imn,category=ca)
                an.save()
                return redirect(animaldisplay)
            return HttpResponse("success")
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,'wallupload.html')


def amoleddisplay(request):
   x=amoleds.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename=i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'amoleddisplay.html',{'mylist':mylist})


def darkdisplay(request):
   x=darks.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'darkdisplay.html',{'mylist':mylist})


def abstractdisplay(request):
   x=abstracts.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'abstractdisplay.html',{'mylist':mylist})


def moviesdisplay(request):
   x=moviess.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'moviesdisplay.html',{'mylist':mylist})


def girldisplay(request):
   x=girls.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'girldisplay.html',{'mylist':mylist})


def naturedisplay(request):
   x=natures.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'naturedisplay.html',{'mylist':mylist})


def animaldisplay(request):
   x=animals.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   print(a)
   mylist=zip(a,b,c)
   return render(request,'animaldisplay.html',{'mylist':mylist})

def index1(request):
    return render(request,'index1.html')


def userregistration(request):
    if request.method=='POST':
        a=uregform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fullname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=uregmodel(fullname=fn, username=un, email=em,password=ps)
            b.save()
            return redirect(userlogin)
        else:
            return HttpResponse('registration failed')
    return render(request,"userregistration.html")

def userlogin(request):
    if request.method=='POST':
        a=uloginform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            b=uregmodel.objects.all()
            c=admins.objects.all()
            for i in b:
                if us==i.username and ps==i.password:
                    return redirect(amoleddisplay)
            else:
                for i in c:
                    if us==i.username and ps==i.password:
                        return redirect(wallupload)
                    else:
                         return HttpResponse("ERROR 404")
    return render(request,"userlogin.html")

def adamoleddisplay(request):
   x=amoleds.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename=i.imagename
       imagename1.append(imagename)
       id= i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'adamoleddisplay.html',{'mylist':mylist})

def amoleddelete(request,id):
    prod=amoleds.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(adamoleddisplay)

def addarkdisplay(request):
   x=darks.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)
       id=i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'addarkdisplay.html',{'mylist':mylist})

def darkdelete(request,id):
    prod=darks.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(addarkdisplay)



def adabstractdisplay(request):
   x=abstracts.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)
       id = i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'adabstractdisplay.html',{'mylist':mylist})

def abstractdelete(request,id):
    prod=abstracts.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(adabstractdisplay)

def admoviesdisplay(request):
   x=moviess.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)
       id=i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'admoviesdisplay.html',{'mylist':mylist})

def moviesdelete(request,id):
    prod=moviess.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(admoviesdisplay)

def adgirldisplay(request):
   x=girls.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)
       id=i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'adgirldisplay.html',{'mylist':mylist})

def girldelete(request,id):
    prod=girls.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(adgirldisplay)


def adnaturedisplay(request):
   x=natures.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename=i.imagename
       imagename1.append(imagename)
       id=i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'adnaturedisplay.html',{'mylist':mylist})

def naturedelete(request,id):
    prod=natures.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(adnaturedisplay)


def adanimaldisplay(request):
   x=animals.objects.all()
   v=x.reverse()
   image1=[]
   category1=[]
   imagename1=[]
   id1=[]

   for i in v:
       path=i.image
       image1.append(str(path).split("/")[-1])
       category=i.category
       category1.append(category)
       imagename = i.imagename
       imagename1.append(imagename)
       id=i.id
       id1.append(id)

   a=image1[ : :-1]
   b=category1[ ::-1]
   c=imagename1[::-1]
   d=id1[::-1]
   print(a)
   mylist=zip(a,b,c,d)
   return render(request,'adanimaldisplay.html',{'mylist':mylist})


def animaldelete(request,id):
    prod=animals.objects.get(id=id)
    if len(prod.image)>0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect(adanimaldisplay)