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


def cart(request):
    id=request.session['logid']
    p=Purchase.objects.all().filter(adm_no=id)
    product=Product.objects.all()
    i=Purchase()
    for i in p:
        a=0
    pl=Plist.objects.all().filter(purch_id=i.purch_id)

    return render(request, 'cart/cart.html',{'k': i , 'pl' : pl, 'product' : product })

def purchase_confirm(request,pk):
    id=request.session['logid']
    remarks = request.POST.get("remarks","")
    uAll=User.objects.all().filter(adm_no=id)
    for u in uAll:
        a=0
    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.remarks=remarks
    pu.placed=1
    pu.save()
    return redirect('/store')
