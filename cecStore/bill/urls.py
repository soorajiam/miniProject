from django.conf.urls import url
from . import views

urlpatterns = [


  #login page redirectin
    url(r'^$',views.bill , name='bill'),
     url(r'^bill1$',views.bill1 , name = 'bill1'),
     url(r'^invoice$',views.invoice , name = 'invoice'),
     url(( r'^c/(?P<pk>[0-9]+)/change/$'), views.qchange, name='response_change'),

]
