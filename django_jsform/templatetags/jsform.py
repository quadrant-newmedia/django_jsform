import json
import time

from django import template
from django.conf import settings
from django.shortcuts import resolve_url
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

def get_errormessage_id(bound_field):
    return f'error-{bound_field.form.prefix}-{bound_field.name}'
def _add_widget_attr(bound_field, name, value):
    _as_widget = bound_field.as_widget
    def as_widget(widget=None, attrs=None, only_initial=False):
        attrs = attrs or {}
        attrs[name] = value
        return _as_widget(widget=widget, attrs=attrs, only_initial=only_initial)
    bound_field.as_widget = as_widget

@register.filter
def with_error_message_container(bound_field):
    error_message_id = get_errormessage_id(bound_field)
    _add_widget_attr(bound_field, 'aria-errormessage', error_message_id)
    return format_html('''
        {field}
        <div class="error" aria-live="polite" id="{error_message_id}"></div>
    ''', field=bound_field, error_message_id=error_message_id)

@register.filter
def with_widget_attr(bound_field, attr):
    # Note - this MUTATES the bound_field
    # You can call this as many times as you like, with different attributes
    # Can be used sort of like django-widget-tweaks to add arbitrary widget attributes from the template
    name, value = attr.split(',', 1)
    _add_widget_attr(bound_field, name, value)
    return bound_field