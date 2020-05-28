import json
import os.path
from django import http

from .templatetags.jsform import get_errormessage_id

def d(text):
    return json.dumps(text)

def js_response(content):
    return http.HttpResponse(content, content_type='text/javascript')

def reload():
    return js_response('location.reload()')

def go_back():
    '''
        This is our recommend response for "Edit" form pages.
        Use with some means of "stale page detection" to trigger the previous page to reload.

        We officially endorse NavTricks.js for "smart back" behaviour.
        https://github.com/quadrant-newmedia/NavTricks

        TODO - add backOrUp([internal_hosts]) function to NavTricks?
    '''
    return js_response(f'''
        if (window.NavTricks) {{
            if (NavTricks.previousPageIsInternal()) {{
                NavTricks.returnToPreviousPage()
            }}
            else {{
                NavTricks.withParentPage(function(p) {{
                    location = p.path
                }})
            }}
        }}
        else {{
            history.back();
        }}
    ''')
    return js_response('history.back()')
def go_to(url):
    '''
        Useful if you have an in-page "Add" form on a list page, and want to navigate to detail page for the created object upon form completion.
    '''
    return js_response(f'location = {d(url)}')
def replace_location(url):
    '''
        We officially endorse NavTricks.js
        https://github.com/quadrant-newmedia/NavTricks
    '''
    return js_response(f'''
        if (window.NavTricks) {{
            NavTricks.replaceCurrentPage({d(url)});
        }}
        else {{
            location.replace({d(url)});
        }}
    ''')

def alert(message, allow_further_submissions=False):
    '''
        Useful for error messages that aren't really typical form error messages, or for actions that are triggered by a simple button push (where there is no corresponding container for error messages).
    '''
    return js_response(f'alert({d(message)}); return {d(allow_further_submissions)}')

def _get_script_content(script_name):
    with open(os.path.join(os.path.dirname(__file__), 'js_helpers', script_name)) as f :
        return f.read()

'''
    Form manipulation helpers.

    Note that we generally recommend using jsform_elementmerge.js and simply returning html pages to be merged into the current document.

    In particular circumstances, you may find it easier to mutate the form directly, and you can use these.

    Note that all of these functions return true, to allow further form submissions.
'''
def reset_form_inputs():
    '''
        Resets form and returns true, to allow further submissions.
    '''
    return js_response(f'form.reset(); return true')

def clear_form_errors():
    '''
        Requires django
        Resets form and returns true, to allow further submissions.
    '''
    return js_response(f'''
        {_get_script_content("clear_form_errors.js")};
        clear_form_errors(form); 
        return true
    ''')
def set_form_errors(form):
    return set_raw_form_errors(
        form.non_field_errors(), 
        {get_errormessage_id(field): field.errors for field in form}
    )
def set_raw_form_errors(form_errors, error_map):
    return js_response(f'''
        {_get_script_content("set_form_errors.js")};
        set_form_errors(form, {d(form_errors)}, {d(error_map)});
        return true
    ''')
def reset_form():js_response(f'''
        {_get_script_content("js_helpers/clear_form_errors.js")};
        clear_form_errors(form); 
        form.reset();
        return true
    ''')