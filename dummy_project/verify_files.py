import json
from django_jsform import js_response

def verify_files(request):
    data = [
        dict(
            name=f.name,
            bytes=f.size,
        )
        for f in request.FILES.getlist('files')
    ]
    return js_response.alert(json.dumps(data, indent=4))

