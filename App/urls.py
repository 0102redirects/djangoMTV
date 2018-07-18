from django.conf.urls import url

from App import views

urlpatterns =[
    url(r'^index/',views.index,name='index'),
    url(r'^uploade/',views.uolade,name='uploade'),
    url(r'^userregister/',views.user_register,name='userregister'),
    url(r'^usercenter/',views.user_center,name='user_center')
]