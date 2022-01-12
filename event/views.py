from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .forms import EventForm
from .models import Event

# Create your views here.
class EventsList(ListView):
    model = Event
    template_name = 'calendar_view.html'

    def get_queryset(self, *args, **kwargs):
        all_events = super(EventsList, self).get_queryset(*args, **kwargs)
        return all_events
       


class EventFormView(CreateView):
    form_class = EventForm
    model = Event
    template_name = 'add_event.html'
    success_url = reverse_lazy('calendar_view')


