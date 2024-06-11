from django.urls import path
from .views import *


urlpatterns = [
    path('',chatbot_view,name='chatbot_view')
]