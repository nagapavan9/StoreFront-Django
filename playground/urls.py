from django.urls import path
from playground import views,templates

#url_configuration
urlpatterns = [
    path('hello/', views.say_hello)
]