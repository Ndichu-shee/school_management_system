from django.contrib.staticfiles.urls import urlpatterns
from django.urls.resolvers import URLPattern
from .views import EventFormView, EventsList
from django.urls import path

urlpatterns=[

    path('',EventsList.as_view(), name='calendar_view'),
    path('add_event/',EventFormView.as_view(),name='add_event'),

]