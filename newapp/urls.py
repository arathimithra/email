from django.urls import path
# from . views import send_test_mail
from . import views

urlpatterns = [
# path('send_mail/',views.send_test_email,name='send_mail')
path('',views.index,name='index')
]
