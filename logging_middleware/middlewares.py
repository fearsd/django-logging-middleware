from loguru import logger
from django.contrib.auth.models import User

class DjangoLoggingMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request headers: {request.headers}")
        logger.info(f"Request user: {request.user}")
        logger.info(f"Request GET data: {request.GET}")
        logger.info(f"Request POST data: {request.POST}")
        logger.info(f"Request FILES data: {request.FILES}")

        response = self.get_response(request)

        logger.info(f"Response status code: {response.status_code}")
        try:
            logger.info(f"Response mediatype: {response.accepted_media_type}")
            logger.info(f"Response _mediatype: {response.charset}")
            logger.info(f"Response data: {response.data}")
        except:
            logger.info(f"Response mediatype: {response.charset}")
            logger.info(f"Response data: {response.content}")
        
        return response


class __TestingMiddleware:
    """
    Needs to set request.user
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        request.user = User.objects.create_user(
            username='jacob', 
            email='jacob@mail.ru', 
            password='top_secret'
        )
        response = self.get_response(request)
        return response
