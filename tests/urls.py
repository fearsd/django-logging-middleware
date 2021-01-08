from django.urls import path

from .views import *

urlpatterns = [
    # function-based views HttpResponse
    path('simple/', simple),
    path('simple_with_query_string/', simple_with_query_string),

    # class-based views HttpResponse
    path('simple/class/', SimpleView.as_view()),
    path('simple/class/with_query_string/', SimpleWithQueryStringView.as_view()),

    # function-based views Response
    path('restframework/simple/', restframework_simple),
    path('restframework/simple_with_query_string/', restframework_simple_with_query_string),

    # class-based views Response
    path('restframework/simple/class/', RestframeworkSimpleView.as_view()),
    path('restframework/simple/class/with_query_string/', RestframeworkSimpleWithQueryStringView.as_view())

]