from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
]
