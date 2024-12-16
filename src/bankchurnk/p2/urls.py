from django.urls import include, path

from . import views

urlpatterns = [
    path('gb_predict/', views.gb_predict, name='gb_predict'),
    path('rdf_predict/', views.rdf_predict, name='rdf_predict'),
    path('xfb_predict/', views.xfb_predict, name='xfb_predict'),
]

