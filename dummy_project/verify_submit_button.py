from django import http

def verify_submit_button(request):
    data = getattr(request, request.method)

    assert 'B' in data
    assert data['B'] == 'buttonB'
    assert 'A' not in data
    assert 'C' not in data

    return http.HttpResponse()
