from django.conf.urls import url
from . import views

urlpatterns = [

    url(( r'^addcart/(?P<pk>[0-9]+)/$'), views.addcart, name='addcart'),
  #login page redirectin
    url(r'^$',views.defaultU , name='all_store'),

    url(( r'^(?P<pk>[0-9]+)/$'), views.DetailView.as_view(), name='detail'),
      #Create the product
      url(r'^add/$', views.ProductCreate.as_view() , name='productadd'),

     url(r'^(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view() , name='productup'),

      url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view() , name='productdel'),
      #url(r'',views.error , name='all_store'),

]
