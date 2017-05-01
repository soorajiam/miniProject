from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^$',views.cart , name='cart'),
url(( r'^purchase/(?P<pk>[0-9]+)/$'), views.purchase_confirm, name='purchase'),

]
