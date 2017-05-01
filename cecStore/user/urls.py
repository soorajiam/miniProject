from django.conf.urls import url
from . import views

urlpatterns = [
  #login page redirectin
  url(r'^loginpage$',views.login , name='login'),

  #Signup page
  url(r'^signuppage$',views.signup , name='signup'),
  #logout page
  url(r'^logout$' , views.logout , name='logout'),
  #signup processing
  url(r'^signup$',views.signupprocess , name='signupprocess'),
  #processing login
  url(r'^login$',views.loginprocess , name = 'loginprocess'),

  url(r'^test$',views.test , name = 'loginprtocess'),

]
