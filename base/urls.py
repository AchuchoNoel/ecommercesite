from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:pk>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
