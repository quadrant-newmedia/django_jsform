from django import http
from django import forms

choices = [
    ['a', 'a'],
    ['b', 'b'],
    ['c', 'c'],
    ['d', 'd'],
]
empty_choices = [['', '-']] + choices

class SimpleForm(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea, initial="blah blah blah...")
    char = forms.CharField(initial="char")
    empty_char = forms.CharField(required=False)
    integer = forms.IntegerField(initial=5)
    empty_integer = forms.IntegerField(initial=5, required=False)
    select = forms.ChoiceField(choices=choices, initial='b')
    multiple_select = forms.MultipleChoiceField(choices=choices, initial=['b','c'])
    empty_select = forms.ChoiceField(choices=empty_choices, required=False)
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, initial='c')
    empty_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, required=False)
    checkboxes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, initial=['a', 'd'])
    hidden = forms.CharField(widget=forms.HiddenInput, initial='secretvalue')

def verify_form(request):
    data = getattr(request, request.method)
    form = SimpleForm(data)

    if form.has_changed() :
        return http.HttpResponseBadRequest(form.changed_data)

    return http.HttpResponse()
