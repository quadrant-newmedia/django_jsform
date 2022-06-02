from django.http import HttpResponse
def view(request):
    return HttpResponse(
        request.POST.urlencode(),
        content_type='text/plain'
    )
