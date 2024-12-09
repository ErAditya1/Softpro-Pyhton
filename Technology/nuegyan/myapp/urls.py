
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('layout', layout, name="layout"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("register/", register, name="register"),
    path("save/", save, name="save"),
    path("login/", login, name="login"),
    path("show/", showdata, name="showdata"),
    path("edit/<int:id>", edit, name="edit"),
    path("delete/<int:id>", delete, name="delete"),
    path("update/<int:id>", update, name="update"),

]
