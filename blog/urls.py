from django.urls import path
from . import views

app_name = 'blog'


'''
Definimos uma lista de url, isto é, os endereços, para renderização das views
Entre <> são os slugs

'''

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),
]