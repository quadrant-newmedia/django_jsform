from django import http
from django.views.generic import View
class view(View):
    def post(self, request):
        return http.HttpResponse()
view = view.as_view()