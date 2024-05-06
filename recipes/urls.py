
from django.urls import path
from recipes.views import index,contato,sobre


urlpatterns = [
    path('',index),
    path('sobre/',sobre),
    path('contato/',contato)

]
