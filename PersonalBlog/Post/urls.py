from django.urls import path,include
from . import views
from .views import home,createpost


urlpatterns = [
    path('',views.home,name='homepage'),
    path('createpost/',views.createpost,name='createpost'),
]
