from django.urls import path
from . import views

urlpatterns = [
    path('wagwan/', views.wagwan, name='wagwan'),

]