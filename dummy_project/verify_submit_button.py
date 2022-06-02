from django import http

def verify_submit_button(request):
    data = getattr(request, request.method)

    assert 'B' in data
    assert data['B'] == 'buttonB'
    assert set(data.keys()) == set(['csrfmiddlewaretoken', 'B', '__hack_ensure_body_not_empty__'])

    return http.HttpResponse()
