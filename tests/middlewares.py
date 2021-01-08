from django.contrib.auth.models import User

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