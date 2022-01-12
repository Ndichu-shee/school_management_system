from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from .views import CourseViewSet, StudentViewSet, TrainerViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet),
router.register(r'trainers',TrainerViewSet),
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('',include(router.urls)),
]