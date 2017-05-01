from django.views import generic
from user.models import User,Batch,Course
from store.models import Product,Purchase,Plist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

def OrdersAdmin(request):
    p=Purchase.objects.all().filter(placed=1)
    l=Plist.objects.all()
    u=User.objects.all()
    product=Product.objects.all()
    return render(request, 'order/orderNA.html',{'u': u , 'p': p , 'l' : l, 'product' : product })

def newOrderAdmin(request):
    p=Purchase.objects.all().filter(placed=1)
    l=Plist.objects.all()
    u=User.objects.all()
    product=Product.objects.all()
    return render(request, 'order/orderNew.html',{'u': u , 'p': p , 'l' : l, 'product' : product })
def response_change(request,pk):

    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.responded=0
    pu.save()
    return redirect('/store')

def order_confirm(request,pk):
    response = request.POST.get("response","")
    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.response=response
    pu.responded=1
    pu.save()
    return redirect('/store')
