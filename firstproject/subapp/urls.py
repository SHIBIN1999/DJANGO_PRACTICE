
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),    
    path('list/',views.list,name='list'),
    path('table/',views.table,name='table'),
    path('delete/<pk>',views.delete,name='delete'),
    path('edit/<pk>',views.edit,name='edit'),
   
]
