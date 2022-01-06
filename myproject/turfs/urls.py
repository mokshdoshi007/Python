from django.contrib import admin
from django.urls import path
from turfs import views

urlpatterns = [

    path('cities/',views.getcity,name='cities'),
    path('city/',views.detail,name='city'),
    path('citybookings/',views.citybookings,name='citybookings'),
    path('singleturf/',views.singleturf,name='singleturf'),
    path('addturf/',views.addturf,name='addturf'),
    path('editslot/',views.editslot,name='editslot'),
    path('getslot/',views.getslot,name='getslot'),
    path('view/',views.view,name='view'),
    path('editturf/',views.editturf,name='editturf'),
    path('bookturf/',views.bookturf,name='bookturf'),
    path('turfbookings/',views.turfbookings,name='turfbookings'),
    path('turfprofile/',views.turfprofile,name='turfprofile'),
    path('turfrecords/',views.turfrecords,name='turfrecords'),

    path('defaultit/',views.defaultit,name='defaultit'),
    path('daychange/',views.daychange,name='daychange'),
]