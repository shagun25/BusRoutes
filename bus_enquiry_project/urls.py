"""
URL configuration for bus_enquiry_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bus_enquiry.views import (
    TransportCompanyViewSet,
    BusViewSet,
    StopViewSet,
    RouteViewSet,
    ScheduleViewSet,
    RouteStopViewSet,
    TransportCompanyViewSet1,
)

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'transport-companies', TransportCompanyViewSet1)
router.register(r'buses', BusViewSet)
router.register(r'stops', StopViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'route-stops', RouteStopViewSet)

urlpatterns = [
    # Your other project-level URLs
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

