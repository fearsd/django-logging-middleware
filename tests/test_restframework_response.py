import pytest

from django.test import TestCase, override_settings
from .utils import MIDDLEWARES_FOR_TESTING

class TestResponseFunctionWithoutUser(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/restframework/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/restframework/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/restframework/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/restframework/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/restframework/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/restframework/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/restframework/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/restframework/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


@override_settings(MIDDLEWARE=MIDDLEWARES_FOR_TESTING)
class TestResponseFunctionWithUser(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/restframework/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/restframework/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/restframework/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/restframework/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/restframework/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/restframework/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/restframework/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/restframework/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


class TestResponseClassWithoutUser(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/restframework/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/restframework/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/restframework/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/restframework/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/restframework/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/restframework/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/restframework/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/restframework/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


@override_settings(MIDDLEWARE=MIDDLEWARES_FOR_TESTING)
class TestResponseClassWithUser(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/restframework/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/restframework/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/restframework/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/restframework/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/restframework/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/restframework/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/restframework/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/restframework/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
