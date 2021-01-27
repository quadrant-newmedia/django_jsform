from django import forms, http
from django.template.response import TemplateResponse

from django_jsform import js_response

class Form(forms.Form):
    name = forms.CharField()

    def clean(self):
        if self.cleaned_data.get('name') :
            self.add_error(None, 'This is a fake form-level error')

def execresponse_test(request):
    # The "error message" form at the bottom is the only one that uses POST
    # This really should go on its own page
    if request.method == 'POST' :
        form = Form(request.POST)
        if not form.is_valid():
            return js_response.set_form_errors(form)
        return js_response.alert('success')

    if 'ACTION' not in request.GET :
        return TemplateResponse(request, 'execresponse_tests.html', {'form': Form()})

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

    if action == 'SUBMITTING_BUTTON_TEST':
        return js_response.JSResponse('alert(submitting_button.innerText);') + js_response.unblock_form()

    return http.HttpResponseBadRequest()


