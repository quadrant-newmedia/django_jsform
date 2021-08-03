from django_jsform import js_response
import json

def view(request):
    return js_response.alert(
        'Success' if request.META.get('HTTP_X_REQUESTED_WITH') == 'jsform' else 'FAIL'
    )