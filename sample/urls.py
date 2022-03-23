from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.InsertRecord),
    path('register',views.Register),
    path('login',views.Login),
    path('logout',views.Logout),
    path('home',views.Home),
    path('otp',views.OtpVerify)
]
