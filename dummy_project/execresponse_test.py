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

    return http.HttpResponseBadRequest()