from django.views.generic import View
from django.http import (
    HttpResponse,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Firstly defining the function based views
def simple(request):
    if request.method == 'GET':
        return HttpResponse("HttpResponse GET function-based view testing")
    elif request.method == 'POST':
        return HttpResponse("HttpResponse POST function-based view testing")
    elif request.method == 'PUT':
        return HttpResponse("HttpResponse PUT function-based view testing")
    elif request.method == 'DELETE':
        return HttpResponse('HttpResponse DELETE function-based view testing')


def simple_with_query_string(request):
    if request.method == 'GET':
        return HttpResponse("HttpResponse GET function-based view with query string testing")
    elif request.method == 'POST':
        return HttpResponse("HttpResponse POST function-based view with query string testing")
    elif request.method == 'PUT':
        return HttpResponse("HttpResponse PUT function-based view with query string testing")
    elif request.method == 'DELETE':
        return HttpResponse('HttpResponse DELETE function-based view with query string testing')

# then class-based views
class SimpleView(View):

    def get(self, request):
        return HttpResponse("HttpResponse GET class-based view testing")
    
    def post(self, request):
        return HttpResponse("HttpResponse POST class-based view testing")
    
    def put(self, request):
        return HttpResponse("HttpResponse PUT class-based view testing")
    
    def delete(self, request):
        return HttpResponse("HttpResponse DELETE class-based view testing")


class SimpleWithQueryStringView(View):

    def get(self, request):
        return HttpResponse("HttpResponse GET class-based view with query string testing")
    
    def post(self, request):
        return HttpResponse("HttpResponse POST class-based view with query string testing")
    
    def put(self, request):
        return HttpResponse("HttpResponse PUT class-based view with query string testing")
    
    def delete(self, request):
        return HttpResponse("HttpResponse DELETE class-based view with query string testing")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def restframework_simple(request):
    if request.method == 'GET':
        return Response({'response': 'Response GET function-based view testing'})
    elif request.method == 'POST':
        return Response({'response': 'Response POST function-based view testing'})
    elif request.method == 'PUT':
        return Response({'response': 'Response PUT function-based view testing'})
    elif request.method == 'DELETE':
        return Response({'response': 'Response DELETE function-based view testing'})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def restframework_simple_with_query_string(request):
    if request.method == 'GET':
        return Response({'response': 'Response GET function-based view with query string testing'})
    elif request.method == 'POST':
        return Response({'response': 'Response POST function-based view with query string testing'})
    elif request.method == 'PUT':
        return Response({'response': 'Response PUT function-based view with query string testing'})
    elif request.method == 'DELETE':
        return Response({'response': 'Response DELETE function-based view with query string testing'})


class RestframeworkSimpleView(APIView):
    def get(self, request):
        return Response({'response': 'Response GET class-based view testing'})
    
    def post(self, request):
        return Response({'response': 'Response POST class-based view testing'})
    
    def put(self, request):
        return Response({'response': 'Response PUT class-based view testing'})
    
    def delete(self, request):
        return Response({'response': 'Response DELETE class-based view testing'})

class RestframeworkSimpleWithQueryStringView(APIView):
    def get(self, request):
        return Response({'response': 'Response GET class-based view with query string testing'})
    
    def post(self, request):
        return Response({'response': 'Response POST class-based view with query string testing'})
    
    def put(self, request):
        return Response({'response': 'Response PUT class-based view with query string testing'})
    
    def delete(self, request):
        return Response({'response': 'Response DELETE class-based view with query string testing'})