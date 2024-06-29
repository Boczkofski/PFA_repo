from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Core"),
    path('add_student', views.add_student, name="add_student")
]
