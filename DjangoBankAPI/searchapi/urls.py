from django.urls import path

from .views import BranchapiView

urlpatterns = [
    path('allbanks/', BranchapiView.as_view(), name='all-banks'),
]
