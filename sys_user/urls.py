from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.login_view, name="views_login"),
    path("login.html", views.login_view, name="views_login"),
    path("login", views.login_view, name="views_login"),
    path("logout", views.logout_view, name="views_logout"),
    path("register", views.register, name="views_register"),
    path("index", views.index, name="views_index"),
    path("accounts/login/", views.index, name="views_accounts_login"),
    path("usercenter", views.usercenter, name="views_usercenter"),
]
