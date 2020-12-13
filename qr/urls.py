from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('details', views.get_details, name="get_details"),
    path('gen_qr' , views.get_qr, name="get_qr"),
    path('fac_details', views.fac_details, name='fac_details'),
    path('scan_qr', views.mark_attendance, name="mark")
]
