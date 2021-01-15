import sys

from django.conf import settings as _settings
from loguru import logger

from .settings import Settings


settings = Settings(_settings)
logger.remove(0)
logger.add(sys.stderr, colorize=True, format=settings.MESSAGE_FORMAT)

class DjangoLoggingMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request URL: {request.get_raw_uri()}")
        logger.info(f"Request METHOD: {request.method}")
        logger.info(f"Request HEADERS: {request.headers}")
        logger.info(f"Request GET data: {request.GET}")
        logger.info(f"Request POST data: {request.POST}")
        logger.info(f"Request FILES data: {request.FILES}")

        response = self.get_response(request)
        logger.info(f"Request USER: {request.user}")
        logger.info(f"Response STATUS_CODE: {response.status_code}")
        try:
            logger.info(f"Response MEDIA_TYPE: {response.accepted_media_type}")
            logger.info(f"Response _MEDIA_TYPE: {response.charset}")
            logger.info(f"Response DATA: {response.data}")
        except:
            logger.info(f"Response MEDIA_TYPE: {response.charset}")
            try:
                logger.info(f"Response DATA: {response.content}")
            except:
                logger.info(f"Response DATA: {response.streaming_content}")
        
        return response
