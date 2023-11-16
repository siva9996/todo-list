from django.urls import path
from .views import TaskList,DetailList,TaskCreate,Taskupdate,Taskdelete,Customloginview,Registerpage
from django.contrib.auth.views import LogoutView


urlpatterns=[
        path('',Customloginview.as_view(),name='login'),
        path('register',Registerpage.as_view(),name='register'),
        path('logout',LogoutView.as_view(next_page='login'),name='logout'),
        path('tasklist',TaskList.as_view(),name='tasks'),
        path('createtask',TaskCreate.as_view(),name='createtask'),
        path('task/<int:pk>/',DetailList.as_view(),name='task'),
        path('taskupdated/<int:pk>/',Taskupdate.as_view(),name='taskupdate'),
        path('taskupdelete/<int:pk>/',Taskdelete.as_view(),name='taskdelete'),
]