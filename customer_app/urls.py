
from django.urls import path
from customer_app import views
urlpatterns = [
    path('', views.home_view,name='home'),
    #path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user,name='logout'),
    path('create/', views.create_customer,name='create-customer'),
    path('retreive/', views.retrieve_customer,name='retrieve-customer'),
    path('detail/<int:pk>', views.customer_detail,name='customer-detail'),
]
# customer_detail/<int:pk>
