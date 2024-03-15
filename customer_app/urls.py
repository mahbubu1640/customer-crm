
from django.urls import path
from customer_app import views
urlpatterns = [
    path('', views.home_view,name='home'),
]
