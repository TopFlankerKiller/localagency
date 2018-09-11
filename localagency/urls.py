"""localagency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from joblist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index,name="index"),
    #### USER CRUD ####
    url(r'^users/',views.user_list,name="users"),
    url(r'^user/new/$',views.UserCreateView.as_view(),name="user_new"),
    url(r'^user/edit/(?P<pk>\d+)/$', views.UserUpdateView.as_view(), name='user_edit'),
    url(r'^user/delete/(?P<pk>\d+)/$', views.UserDeleteView.as_view(), name='user_delete'),
    url(r'^user/view/(?P<pk>\d+)/$',views.user_view,name="user_view"),
    #### OCCUPATION CRUD ####
	url(r'^occupations/',views.occupation_list,name="occupations"),
	url(r'^occupation/new/$',views.OccupationCreateView.as_view(),name="occupation_new"),
    url(r'^occupation/edit/(?P<pk>\d+)/$', views.OccupationUpdateView.as_view(), name='occupation_edit'),
    url(r'^occupation/delete/(?P<pk>\d+)/$', views.OccupationDeleteView.as_view(), name='occupation_delete'),
    url(r'^occupation/view/(?P<pk>\d+)/$',views.occupation_view,name="occupation_view"),
    #### USERHASOCCUPATION CRUD ####
	url(r'^userhasoccupations/',views.userhasoccupation_list,name="userhasoccupations"),
	url(r'^userhasoccupation/new/$',views.UserhasoccupationCreateView.as_view(),name="userhasoccupation_new"),
    url(r'^userhasoccupation/edit/(?P<pk>\d+)/$', views.UserhasoccupationUpdateView.as_view(), name='userhasoccupation_edit'),
    url(r'^userhasoccupation/delete/(?P<pk>\d+)/$', views.UserhasoccupationDeleteView.as_view(), name='userhasoccupation_delete'),
    #### NEW CONNECTION ####
    url(r'^connection/',views.new_connection,name="connection"),

]
