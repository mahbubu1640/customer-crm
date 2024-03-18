
from django.urls import path
from customer_app import views
urlpatterns = [
    path('', views.home_view,name='home'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
]
