from loguru import logger


class DjangoLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request headers: {request.META}")
        logger.info(f"Request user: {request.user}")
        logger.info(f"Request GET data: {request.GET}")
        logger.info(f"Request POST data: {request.POST}")
        logger.info(f"Request FILES data: {request.FILES}")

        response = self.get_response(request)

        logger.info(f"Response status code: {response.status_code}")
        try:
            logger.info(f"Response mediatype: {response.accepted_media_type}")
            logger.info(f"Response _mediatype: {response.charset}")
        except:
            logger.info(f"Response mediatype: {response.charset}")
        logger.info(f"Response data: {response.data}")

        return response
