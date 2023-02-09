from django.urls import path

from webapp.views.base import index
from webapp.views.cat import cat

urlpatterns = [
    path('', index, name='index'),
    path('cat', cat, name='cat'),
]