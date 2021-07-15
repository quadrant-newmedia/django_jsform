from django import http
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .form_test_view import FormTestView

from . import simple_form
from .verify_files import verify_files
from .verify_submit_button import verify_submit_button
from .execresponse_test import execresponse_test
from .elementmerge_test import elementmerge_test

from .filter_form import filter_form

def import_view(module, view_name='view', package_name=__package__):
    from importlib import import_module
    return getattr(import_module(module, package_name), view_name)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('200/', lambda r: http.HttpResponse()),

    # This is a test of our templates, and their usage with set_form_errors
    # For live "playground" type testing
    path('form_test/', FormTestView.as_view()),

    path('jsform_tests/', TemplateView.as_view(template_name='jsform_tests.html', extra_context=dict(
        simple_form=simple_form.SimpleForm(),
    ))),
    path('verify_simple_form/', simple_form.verify_form),
    path('verify_files/', verify_files),
    path('verify_submit_button/', verify_submit_button),

    path('execresponse_tests/', execresponse_test),

    path('elementmerge_tests/', elementmerge_test),

    path('filter_form/', filter_form),
    path('verify_attrs/', import_view('.verify_attrs')),
]
