from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("Master/index", views.admin_index, name="admin_index"),
    path("Master/teacher", views.teachers, name="teacher"),
    path("Master/teacher-add", views.teacher_add, name="teacher-add"),
]
