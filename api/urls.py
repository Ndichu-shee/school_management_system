from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from .views import CourseViewSet, StudentViewSet, TrainerViewSet
from rest_framework_swagger.views import get_swagger_view
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet),
router.register(r'trainers',TrainerViewSet),
router.register(r'courses', CourseViewSet),

schema_view = get_swagger_view(title='School management API')


urlpatterns = [
    path('^$', schema_view),
    path('',include(router.urls)),
]