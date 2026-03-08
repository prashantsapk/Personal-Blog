from django.urls import path,include
from . import views
from .views import home,createpost,signupview,loginview,delete_post


urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signupview,name='signup'),
    path('login/',views.loginview,name='login'),
    path('deletepost/',views.delete_post,name='deletepost'),
    path('createpost/',views.createpost,name='createpost'),
]
