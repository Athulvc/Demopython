from. import views
from django.contrib import admin
from django.urls import path, include
app_name = 'todo_app'

urlpatterns = [
    path('',views.add, name='add'),
    path('delete/<int:taskid>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update, name='update'),
    path('cbvhome /',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]