"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from source.views import *
from source.API.routers import source_urlparttern
from rest_framework import permissions
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version='v1',
        description="UI for API",
        contact=openapi.Contact(email="gin21010304@gmail.com"),
        license=openapi.License(name="Thanh Nhan"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name= 'index'),
    path('home/',HomeView.as_view(), name='home'),
    path('login/',LoginView .as_view(), name ='login'),
    path('signup/',SignupView.as_view(),name = 'signup'),
    path('logout/', LogoutView.as_view(), name='logout'),  
     path('mark_as_done/<int:task_id>/', MarkAsDoneView.as_view(), name='mark_as_done'),
    path('delete_task/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('add/',AddPostView.as_view(),name='add_task'),
    path('API/', include(source_urlparttern)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


