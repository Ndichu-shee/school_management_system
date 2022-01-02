from django.urls import path
from .views import TrainerList, TrainersFormView, delete_trainer, edit_trainer,  trainer_profile
from . import views 

urlpatterns =[
    path ('', TrainerList.as_view(), name='trainers_list'),
    path ('add_trainer/',TrainersFormView.as_view(), name='add_trainer'),
    path ('<id>/delete', delete_trainer, name = 'delete_trainer'),
    path('<id>/edit',edit_trainer, name='edit_trainer'),
    path('<id>/view',trainer_profile, name='trainer_profile'),
]
