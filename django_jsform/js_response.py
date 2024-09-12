import json
import os.path
from typing import Any, Dict, List, Union

from django import forms, http
from django.forms.utils import ErrorList
from typing_extensions import Literal

from .templatetags.jsform import get_errormessage_id


def d(text: Any):
    return json.dumps(text)


class JSResponse(http.HttpResponse):
    """
    HttpResponse subclass that:
        - sets correct content_type
        - can be added together (to concatenate the javascript statements in each)
    """

    def __init__(self, content: str):
        self._string_content = content
        super().__init__(content, content_type="text/javascript")

    def __add__(self, other: "JSResponse"):
        return JSResponse(";".join([self._string_content, other._string_content]))


def js_response(content: str):
    """
    Kept for backward compatibility.
    Users might as well use JSResponse directly.
    """
    return JSResponse(content)


def reload():
    return js_response("location.reload()")


def go_back():
    """
    This is our recommend response for "Edit" form pages.
    Use with some means of "stale page detection" to trigger the previous page to reload.

    We officially endorse NavTricks.js for "smart back" behaviour.
    https://github.com/quadrant-newmedia/NavTricks

    TODO - add backOrUp([internal_hosts]) function to NavTricks?
    """
    return js_response("""
        if (window.NavTricks) {
            if (NavTricks.previousPageIsInternal()) {
                NavTricks.returnToPreviousPage()
            }
            else {
                NavTricks.withParentPage(function(p) {
                    location = p.path
                })
            }
        }
        else {
            history.back();
        }
    """)


def go_to(url: str):
    """
    Useful if you have an in-page "Add" form on a list page, and want to navigate to detail page for the created object upon form completion.
    """
    return js_response(f"location = {d(url)}")


def replace_location(url: str):
    """
    NOT RECOMMENDED.
    """
    return js_response(f"""
        location.replace({d(url)});
    """)


def unblock_form():
    return js_response("""form.removeAttribute('block-submissions')""")


def _optional_unblock(unblock: bool):
    return unblock_form() if unblock else js_response("")


def _optional(possible_js_response: Union[None, Literal[False], JSResponse]):
    """
    Helper function which makes it easier to (conditionally) add different JSResponse objects together
    """
    if possible_js_response:
        return possible_js_response
    return JSResponse("")


def alert(message: str, allow_further_submissions: bool = False):
    """
    Useful for error messages that aren't really typical form error messages, or for actions that are triggered by a simple button push (where there is no corresponding container for error messages).

    Note - allow_further_submissions is so-called for backward compatibility. In other functions, we've renamed it to "unblock".
    """
    return js_response(f"alert({d(message)});") + _optional_unblock(
        allow_further_submissions
    )


def _get_script_content(script_name: str):
    with open(os.path.join(os.path.dirname(__file__), "js_helpers", script_name)) as f:
        return f.read()


"""
    Form manipulation helpers.

    Note that we generally recommend using jsform_elementmerge.js and simply returning html pages to be merged into the current document.

    In particular circumstances, you may find it easier to mutate the form directly, and you can use these.

    Note that all of these functions return true, to allow further form submissions.
"""


def reset_form_inputs(unblock: bool = True):
    """
    Resets form and unblocks forms
    """
    return js_response("form.reset();") + _optional_unblock(unblock)


def clear_form_errors(unblock: bool = True):
    """
    Requires django
    Resets and unblocks form.
    """
    return js_response(f"""
        {_get_script_content("clear_form_errors.js")};
        clear_form_errors(form); 
    """) + _optional_unblock(unblock)


def set_form_errors(
    form: forms.BaseForm,
    status_code: int = 400,
    unblock: bool = True,
    focus_errors: bool = True,
):
    return set_raw_form_errors(
        form.non_field_errors(),
        {get_errormessage_id(field): field.errors for field in form},
        status_code,
        unblock=unblock,
        focus_errors=focus_errors,
    )


def set_raw_form_errors(
    form_errors: "List[str]|ErrorList",
    error_map: Dict[str, "List[str]|ErrorList"],
    status_code: int = 400,
    unblock: bool = True,
    focus_errors: bool = True,
):
    r = (
        js_response(f"""
        {_get_script_content("set_form_errors.js")};
        set_form_errors(form, {d(form_errors)}, {d(error_map)});
    """)
        + _optional_unblock(unblock)
        + _optional(focus_errors and focus_form_errors())
    )
    r.status_code = status_code
    return r


def focus_form_errors():
    return js_response(f"""
        {_get_script_content("focus_form_errors.js")};
        focus_form_errors(form);
    """)


def reset_form(unblock: bool = True):
    return js_response(f"""
        {_get_script_content("clear_form_errors.js")};
        clear_form_errors(form); 
        form.reset();
    """) + _optional_unblock(unblock)
