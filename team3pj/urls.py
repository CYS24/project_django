from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),    
    path('login_ok/', views.login_ok, name='login_ok'),
    path('register/', views.register, name='register'),
    path('register_ok/', views.register_ok, name='register_ok'),    
    path('logout/', views.logout, name='logout'),
    path('password/', views.password, name='password'),
    path('modaltest/<int:id>', views.modaltest, name='modaltest'),
    #################################
    path('tables', views.tables, name='tables'),
    path('write/', views.write, name='write'),
    path('write/write_ok/', views.write_ok, name='write_ok'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'),
    path('content/<int:id>', views.content, name='content'),    
]