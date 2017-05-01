from django.views import generic
from .models import User,Batch,Course
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone




def login(request):
    return render(request, 'user/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/products/')
    u=User.objects.all()


def signup(request):
    return render(request, 'user/register.html' )

def test(request):
    return render(request, 'user/test.html' )



def loginprocess(request):
    adm_no =  request.POST.get("username","")
    password = request.POST.get("password","")
    if(len(adm_no) == 0 and len(password) == 0):
        return render(request,'user/login.html',{'loginmessage' : ''  })
    user_data = User.objects.all().filter(adm_no = adm_no)
    got = True
    for e in user_data:
        got = False
    if(got):
        return render(request,'user/login.html',{'loginmessage' : 'Email id Does Not Exist Please Signup '})

    for e in user_data:
        if(e.password != password):
            return render(request,'user/login.html',{'loginmessage' : 'Password/Emailid entered is wrong please Try again' })
    '''if(_ver == 0):
            return render(request,'verified.html', {'id' : _id} )'''
    request.session['logid'] = adm_no
    return HttpResponseRedirect('/store')

def signupprocess(request):
    password = request.POST.get('password','')
    name = request.POST.get('name','')
    phone = request.POST.get('phonenumber','')
    cbid = request.POST.get('cbid','')
    '''vericode = '000000'
    verified = '0'	'''
    adm_no = request.POST.get('email','')
    val=1
    batch = Batch.objects.all()
    for i in batch:
        if(i.cbid == cbid): val=0;break
    dict = {'name' : name , 'batch': batch , 'phonenumber' : cbid,'cbid' : phone,'adm_no' : adm_no, 'message' : 'Error'}
    if(password == '' or  password.__len__() >= 100 or password.__len__() <= 7):
        dict['signupmessage'] = "Enter a valid password ** It should contain more than 7 charecters ** "
        return render(request,'user/register.html',dict)
    elif(name == ''):
        dict['signupmessage'] = "Enter a valid name"
        return render(request,'user/register.html',dict)
    elif(adm_no == '' ):
        dict['signupmessage'] = "Enter a valid admission number"
        return render(request,'user/register.html',dict)
    elif(val==1):
        dict['signupmessage']="enter a valid course/class"
    '''try:
        phone = int(phone)
    except Exception, e:
        dict['signupmessage'] = "Enter a valid phone number"
        return render(request,'user/register.html',dict)'''
    data = User.objects.all()
    email_check = User.objects.all().filter(adm_no = adm_no)
    for y in email_check :
        dict['signupmessage'] = "This adm_no is already in use . Please try again with another adm_no "
        return render(request,'user/register.html',dict)
    request.session['logid'] = adm_no


    p = User(name = name,password=password,adm_no=adm_no,phone_no =phone,cbid=i)
    p.save()
    return render(request, 'user/login.html' , {'loginmessage' : " Signup Completed Please check Email and Login to continue "})
