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

def bill(request):
    product=Product.objects.all()
    pr=Purchase.objects.all().filter(placed=64).filter(adm_no=1)
    l=Plist.objects.all()

    product=Product.objects.all()
    return render(request, 'bill/bill.html',{'product':product, 'pr': pr , 'l' : l })
    return redirect('/bill')

def bill1(request):
        pk=request.POST.get("prod","")
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
            pu=Purchase(adm_no=u,purchase_date=timezone.now(),total=pr.price,remarks='',response='',responded=0,placed=64)

        j=0

        pu.save()

        pl=Plist(purch_id=pu,product_id=pr,price=pr.price,quantity=1)
        pl.save()
        pl=Plist.objects.all().filter(purch_id=pu.purch_id)
        for pls in pl:
            j=j+pls.price
        pu.total=j
        pu.placed=64
        pu.save()
        return redirect('/bill')
def invoice(request):
    pr=Purchase.objects.all().filter(placed=64).filter(adm_no=1)
    for p in pr:
        product=Product.objects.all()
        pr=Purchase.objects.all().filter(placed=64).filter(adm_no=1)
        l=Plist.objects.all()

        product=Product.objects.all()
        return render(request, 'bill/invoice.html',{'product':product, 'pr': pr , 'l' : l })
        return redirect('/bill')

        p.responded=1
        p.save()

def qchange(request,pk):
    id=request.session['logid']
    q=int(request.POST.get("quantity",""))
    pl=Plist.objects.all().filter(tfield=pk)
    for i in pl:
        a=0
    p=Plist()
    i.quantity=q
    j=Product()

    p=Product.objects.all()
    for j in p:
        if (j==i.product_id):
            i.price=q*j.price
            j.quantity-=q
            i.save()
            j.save()
            if (id==64):
                return redirect('/bill')
            else:
                return redirect('/cart')


        return redirect('/cart')
