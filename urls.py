from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   # path('',views.index,name='index'),
    path('',views.prime,name='prime'),
    path('first/',views.first,name='first'),
    path('submit/',views.submit,name='submit'),
    path('listfirst/',views.listfirst,name='listfirst'),
    path('updatefirst/<int:dataid>',views.updatefirst,name='updatefirst'),
    path('updatereg/<int:dataid>',views.updatereg,name='updatereg'),
    path('deletefirst/<int:dataid>',views.deletefirst,name='deletefirst'),
    path('index/',views.index,name='index')
    

]
