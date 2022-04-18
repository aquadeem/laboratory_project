"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from laboratory.views import IndexView, StudentListView, StudentListUpdate, StudentListDelete,\
    StudentListAdd, StudentListDetail, base_template, get_reset_password, get_welcome_email, get_email_verification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('base/', base_template),
    path('reset_password/', get_reset_password),
    path('welcome_email/', get_welcome_email),
    path('email_verification/', get_email_verification),
    path('list_student/', StudentListView.as_view(), name='list_student'),
    path('info_student/<int:pk>', StudentListDetail.as_view(), name='info_student'),
    path('update_student/<int:pk>', StudentListUpdate.as_view(), name='update_student'),
    path('delete_student/<int:pk>', StudentListDelete.as_view(), name='delete_student'),
    path('add_student/', StudentListAdd.as_view(), name='add_student')
]
