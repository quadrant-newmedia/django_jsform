from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .form_test_view import FormTestView

urlpatterns = [
    path('form_test/', FormTestView.as_view()),
]
