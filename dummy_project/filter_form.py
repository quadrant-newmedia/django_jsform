import json
from django import forms
from django.template.response import TemplateResponse

class Form(forms.Form):
    search = forms.CharField()

def filter_form(request):
    result = None
    if request.GET :
        form = Form(request.GET)
        if form.is_valid() :
            result = json.dumps(form.cleaned_data)
    else :
        form = Form()

    return TemplateResponse(request, 'filter_form.html', dict(
        form=form,
        result=result,
    ))