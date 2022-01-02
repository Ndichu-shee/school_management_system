from django.http.response import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView
from .models import Trainer
from django.views.generic import ListView
from .forms import TrainerForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.



class TrainerList(ListView):
    model = Trainer
    template_name = 'trainers_list.html'

    def get_queryset(self, *args, **kwargs):
        all_trainers = super(TrainerList, self).get_queryset(*args, **kwargs)
        return all_trainers

class TrainersFormView(CreateView):
    form_class =  TrainerForm
    model = Trainer
    template_name = 'add_trainer.html'
    success_url =reverse_lazy('trainers_list')

def delete_trainer(request, id):
    trainer = Trainer.objects.get(id = id)

    if request.method == "POST":
        trainer.delete()
        return redirect("/trainers/")
    return render(request, 'delete_trainer.html', {'trainer': trainer})

def edit_trainer(request, id):
    context = {}

    trainer= Trainer.objects.get( id = id)
    form =TrainerForm(request.POST or None, instance = trainer)


    if form.is_valid():
        form.save()
        return redirect("/trainers/")
    context["form"] = form

    return render(request, "edit_trainer.html", context)


def trainer_profile(request, id):
    trainer = Trainer.objects.get(id = id)
    return render (request, 'trainer_profile.html', {'trainer': trainer})

