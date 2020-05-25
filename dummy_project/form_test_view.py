from django import forms
from django.template.response import TemplateResponse
from django.views.generic import View

from django_jsform import js_response

class Form(forms.Form):
    name = forms.CharField(help_text="Please give your full name")
    favourite_colour = forms.ChoiceField(choices=[
        ['', '-----'],
        ['red', 'red'],
        ['green', 'green'],
        ['blue', 'blue'],
    ])
    favourite_colour_radio = forms.ChoiceField(choices=[
        ['red', 'red'],
        ['green', 'green'],
        ['blue', 'blue'],
    ], widget=forms.RadioSelect)
    favourite_colours = forms.MultipleChoiceField(choices=[
        ['red', 'red'],
        ['green', 'green'],
        ['blue', 'blue'],
    ], widget=forms.CheckboxSelectMultiple)
    certify = forms.BooleanField(label="I certify that this is correct.")

class FormTestView(View):
    def get(self, request):
        return TemplateResponse(request, 'django_jsform/form_test.html', dict(form=Form(initial=dict(
            do_you_agree='a',
            do_you_agree_radio=None,
        ))))

    def post(self, request):
        form = Form(request.POST)

        if not form.is_valid() :
            return js_response.set_form_errors(form)

        return js_response.alert('Success!');