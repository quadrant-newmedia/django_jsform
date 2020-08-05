import time
from django import forms
from django.template.response import TemplateResponse

choices = [
    ['a', 'a'],
    ['b', 'b'],
    ['c', 'c'],
    ['d', 'd'],
]

class Form(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea)
    char = forms.CharField()
    empty_char = forms.CharField()
    select = forms.ChoiceField(choices=choices)
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
    checkboxes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices)
    file = forms.FileField()

def get_form(request):
    if request.method == 'GET':
        return Form()
    form = Form(request.POST, request.FILES)
    form.is_valid()
    return form

def elementmerge_test(request):
    return TemplateResponse(request, 'elementmerge_test.html', dict(
        form=get_form(request),
        result=time.time(),
    ))