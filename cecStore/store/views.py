from django.views import generic
from user.models import User,Batch,Course
from .models import Product,Purchase,Plist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone



# Create your views here.
def defaultU(request):
    proList=Product.objects.all()
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'user/login.html',{'loginmessage' : 'Please Login to Continue'  })

    usrs=User.objects.all().filter(adm_no=id)
    for u in usrs:
        a=0
    if(u.isadmin==64):
        return render(request, 'store/inventory.html',{'proList': proList })
    return render(request, 'store/products.html',{'proList': proList })

def addcart(request,pk):
    id=request.session['logid']
    uAll=User.objects.all().filter(adm_no=id)
    for u in uAll:
        a=0
    pre=Product.objects.all().filter(product_id=pk)
    for pr in pre:
        a=0
    p=Purchase.objects.all()
    j=a
    pu=Purchase()
    for pu in p:
        if(pu.adm_no==u and pu.responded==0):
            a=1

    if(pu.responded!=0):
        a=0
    j=pu.total+pr.price
    if(a==0):
        pu=Purchase(adm_no=u,purchase_date=timezone.now(),total=pr.price,remarks='',response='',responded=0)

    j=0

    pu.save()

    pl=Plist(purch_id=pu,product_id=pr,price=pr.price,quantity=1)
    pl.save()
    pl=Plist.objects.all().filter(purch_id=pu.purch_id)
    for pls in pl:
        j=j+pls.price
    pu.total=j
    pu.save()
    pr.quantity-=1
    pr.save()

    return redirect('/store')




    return redirect('/store')

class DetailView(generic.DetailView):

    model=Product
    template_name='store/detail.html'


class ProductCreate (CreateView):
    model=Product
    fields=['pname','p_short','price','quantity','product_type','brand_name','mrp','seller','desc','spec','image']

class ProductUpdate (UpdateView):
    model=Product
    fields=['pname','p_short','price','quantity','product_type','brand_name','mrp','seller','desc','spec','image']

class ProductDelete (DeleteView):
    model=Product
    success_url='/store/'
def error(request):
    return render(request, 'store/defaultU.html')
