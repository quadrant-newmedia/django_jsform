import json
from django import http

def d(text):
    return json.dumps(text)

def js_response(content):
    return http.HttpResponse(content, content_type='text/javascript')

# Helper for combining the instructions of multiple responses
# see reset_form for sample
def multi_response(*responses):
    return js_response(';'.join([r.content.decode(r.charset) for r in responses]))

def reload():
    return js_response('location.reload()')

def go_back():
    '''
        This is our recommend response for "Edit" form pages.
        Use with some means of "stale page detection" to trigger the previous page to reload.
    '''
    return js_response('history.back()')
def close_window(fallback_url='/'):
    '''
        Useful if form page is opened in new widow (ie. for a complex multi-step form).
        We don't recommend this, though. Try to open form in same window, and use go_back() when done.
    '''
    return js_response(f'window.close();location={d(fallback_url)}')
def go_to(url):
    '''
        Useful if you have an in-page "Add" form on a list page, and want to navigate to detail page for the created object upon form completion.
    '''
    return js_response(f'location = {d(url)}')
def replace_location(url):
    '''
        Useful for "Add" form pages, where you want to view the created object after form completion, but want to remove the form page from history.

        For most purposes, location.replace(url) would be enough.

        The history.replaceState bit changes what the document.referrer will be on the next page, which is needed if the next page relies on the referrer to, ie., generate a back button with the title of the previous page.

        TODO - we should either:
            resolve url relative to current page, as is done in qnc_crud/utils.js in [qnc-replace-location] handler
            only accept absolute/site-relative urls
    '''
    return js_response(f'''
        try {{
            history.replaceState(null, '', document.referrer);
        }}
        catch (e) {{}}
        // replaceState is asynchronous - if we do location.replace immediately, next page won't have the modified referrer
        setTimeout(function() {{
            location.replace({d(url)});
        }}, 0);

        // prevent further form submissions
        return true
    ''')

def alert(message):
    '''
        Useful for error messages that aren't really typical form error messages, or for actions that are triggered by a simple button push (where there is no corresponding container for error messages).
    '''
    return js_response(f'alert({d(message)})')