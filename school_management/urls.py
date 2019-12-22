"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
#from rest_framework import routers
from rest_framework_nested import routers
from student.views import *

router = routers.SimpleRouter()
router.register(r'students', StudentAPI)
router.register(r'schools', SchoolAPI)

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
school_router.register(r'students', StudentViewSet, basename='school-student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(school_router.urls)),
]
