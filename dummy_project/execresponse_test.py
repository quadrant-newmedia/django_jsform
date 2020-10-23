from django import http
from django.template.response import TemplateResponse

from django_jsform import js_response

def execresponse_test(request):
    if 'ACTION' not in request.GET :
        return TemplateResponse(request, 'execresponse_tests.html', {})

    action = request.GET['ACTION']

    if action == 'ALERT':
        return js_response.alert('Hooray!')
    if action == 'ALERT_MULTIPLE':
        return js_response.alert('Hooray!', True)
    if action == 'BACK':
        return js_response.go_back()
    if action == 'ALERT_400':
        r = js_response.alert('Custom message with non 2XX response')
        r.status_code = 400
        return r

    # TODO - test each method from js_response?
    if action == 'RESET':
        return js_response.reset_form()

    return http.HttpResponseBadRequest()