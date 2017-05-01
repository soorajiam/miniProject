from django.conf.urls import url
from . import views

urlpatterns = [


  #login page redirectin
    url(r'^history/$',views.OrdersAdmin , name='OrderNA'),
    url(r'^new/$',views.newOrderAdmin , name='OrderNew'),
     url(( r'^response/(?P<pk>[0-9]+)/$'), views.order_confirm, name='response'),
     url(( r'^response_change/(?P<pk>[0-9]+)/$'), views.response_change, name='response_change'),


]
