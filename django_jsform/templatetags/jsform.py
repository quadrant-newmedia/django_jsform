from typing import Optional

import html_generators as h
from django import forms, template
from django.forms import Widget
from django.forms.boundfield import BoundField
from django.utils.html import format_html

register = template.Library()


def get_errormessage_id(bound_field: BoundField) -> str:
    return f"error-{bound_field.html_name}"


def _add_widget_attr(bound_field: BoundField, name: str, value: h.Content):
    _as_widget = bound_field.as_widget

    def as_widget(
        widget: Optional[Widget] = None,
        attrs: h.Content = None,
        only_initial: bool = False,
    ):
        attrs = attrs or {}
        attrs[name] = value
        return _as_widget(widget=widget, attrs=attrs, only_initial=only_initial)

    bound_field.as_widget = as_widget


@register.filter
def is_single_checkbox(bound_field: BoundField) -> bool:
    return isinstance(bound_field.field, forms.BooleanField)


@register.filter
def with_error_message_container(bound_field: BoundField):
    """
    Render field with error message container (div) underneath it
    """
    return format_html(
        """
        {field}
        {error_message_container}
    """,
        field=with_error_attributes(bound_field),
        error_message_container=error_message_container(bound_field),
    )


@register.filter
def with_error_attributes(bound_field: BoundField):
    """
    Mutate the BoundField so that it passes some extra attrs to the widget when rendering.

    Can be used in conjunction with error_message_container when with_error_message_container is not flexible enough (when you want a different layout).
    """
    error_message_id = get_errormessage_id(bound_field)
    bound_field._error_message_id = error_message_id  # type: ignore [reportAttributeAccessIssue]
    _add_widget_attr(bound_field, "aria-errormessage", error_message_id)
    if bound_field.errors:
        _add_widget_attr(bound_field, "aria-invalid", "true")
    return bound_field


@register.filter
def error_message_container(bound_field: BoundField):
    """
    Important: we always generate the error message container, even if empty.

    This is important, because aria-live only works for elements that are initially in the DOM.

    It also makes it easier to add error messages later via js (see how js_response.set_form_errors() works).

    Lastly, jsform_elementmerge.js doesn't work as desired if you have "optional" elements with any subsequent siblings, so it's always best to put them in their own container.
    """
    try:
        error_message_id = bound_field._error_message_id  # type: ignore
    except AttributeError:
        # Note: the user has likely already rendered this BoundField, so it would do no good for us to call with_error_attributes() on it now.
        # Better to raise an exception to force them to deal with the issue.
        raise Exception(
            'You must call "with_error_attributes(bound_field)" on the bound field before you call this function (or the field won\'t be rendered with the correct attributes to link it to this error message container'
        )
    return format_html(
        """\
        <div class="error" aria-live="polite" id="{error_message_id}">{errors}</div>
    """,
        error_message_id=error_message_id,
        errors=". ".join(bound_field.errors),
    )


@register.filter
def with_widget_attr(bound_field: BoundField, attr: str):
    # Note - this MUTATES the bound_field
    # You can call this as many times as you like, with different attributes
    # Can be used sort of like django-widget-tweaks to add arbitrary widget attributes from the template
    name, value = attr.split(",", 1)
    _add_widget_attr(bound_field, name, value)
    return bound_field
