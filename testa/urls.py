from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('record/<int:pk>', views.customer_record, name='record'),
   path('logout_user', views.logout_user, name='logout'),
   path('register_user', views.register_user, name='register'),
]
