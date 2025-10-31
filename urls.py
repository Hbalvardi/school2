from django.contrib import admin
from django.urls import path
from . import views

app_name="class"

urlpatterns = [
    # path('blog_detail/',views.blog_detail,name="blog_detail"),
    # path('manage-students/',views.manage_students,name="manage-students"),
    # path('messages/',views.messages,name="messages"),
    # # path('my-profile/',views.home,name="my-profile"),
    # path('teacher-action/',views.teacher,name="teacher-action"),
    # path('',views.home,name="home"),
    # path('news/',views.news,name="news"),
    # path('create_class/',views.create_class,name="create_class"),
    # path('base/',views.base,name="base"),
    path('',views.home,name='home')
   
    
]