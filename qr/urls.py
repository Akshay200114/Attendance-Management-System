from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('details', views.get_details, name="get_details"),
    path('gen_qr' , views.get_qr, name="get_qr")
]
