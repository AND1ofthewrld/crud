from django.urls import path
from .views import check_collection

urlpatterns = [
    path('check/', check_collection, name='check_collection'),

]