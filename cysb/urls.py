from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('write/write_ok/', views.write_ok, name='write_ok'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'),
    ####################################################################
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bwrite/bwrite_ok/', views.bwrite_ok, name='bwrite_ok'),
    path('bcontent/<int:id>', views.bcontent, name='bcontent'),
    path('bupdate/<int:id>', views.bupdate, name='bupdate'),
    path('bupdate/bupdate_ok/<int:id>', views.bupdate_ok, name='bupdate_ok'),
    path('bdelete/<int:id>', views.bdelete, name='bdelete'),
    ########################################################
    path('login/', views.login, name='login'),    
    path('login/login_ok/', views.login_ok, name='login_ok'),
    path('logout/', views.logout, name='logout'),    
    #############################################
    path('template1/', views.test1, name='template1'),
    path('template2/', views.test2, name='template2'),
    path('template3/', views.test3, name='template3'),
    path('template4/', views.test4, name='template4'),
    path('template5/', views.test5, name='template5'),
    path('template6/', views.test6, name='template6'),
    path('template7/', views.test7, name='template7'),
    path('template8/', views.test8, name='template8'),
]