from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('addtodo/',views.addtodo,name='addtodo'),
    path('deletetodo/<str:pk>/',views.deletetodo,name='deletetodo')
]