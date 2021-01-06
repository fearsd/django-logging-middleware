from django.views.generic import View
from django.http import (
    HttpResponse, 
    HttpResponseBadRequest, 
    HttpResponseForbidden, 
    Http404, 
    HttpResponseGone, 
    HttpResponseNotAllowed, 
    HttpResponseNotFound, 
    HttpResponseNotModified,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    HttpResponseServerError,
    StreamingHttpResponse
)


# Firstly defining the function based views
def get_simple(request):
    if request.method == 'GET':
        return HttpResponse("HttpResponse testing")