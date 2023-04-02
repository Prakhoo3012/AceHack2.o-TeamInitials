from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logid", views.log_id, name="log"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add", views.add, name="add"),
    path("send", views.start, name="send"),
    path("sendt", views.send_end, name="see"),
    path("result", views.result, name="result"),
    path("sidebar", views.navbar, name="navbar"),
    path("nav", views.nav, name="nav"),
    path("info", views.personaal_info, name="info"),
    path("timetable", views.timetable, name="timetable"),
    path("assignment", views.assignment, name="assignment"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
]
