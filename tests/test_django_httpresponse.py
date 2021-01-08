import pytest

from django.test import TestCase, override_settings

from .utils import MIDDLEWARES_FOR_TESTING


class TestHttpResponseFunctionWithoutUserMiddleware(TestCase):
    
    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


@override_settings(MIDDLEWARE=MIDDLEWARES_FOR_TESTING)
class TestHttpResponseFunctionWithUserMiddleware(TestCase):
    
    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/simple/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/simple/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/simple_with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/simple_with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


class TestHttpResponseClassWithoutUserMiddleware(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")


@override_settings(MIDDLEWARE=MIDDLEWARES_FOR_TESTING)
class TestHttpResponseClassWithUserMiddleware(TestCase):

    def test_middleware_simple_get_request(self):
        try:
            self.client.get('/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_request(self):
        try:
            self.client.post('/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_request(self):
        try:
            self.client.put('/simple/class/', data={'data': 'data'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")

    def test_middleware_simple_delete_request(self):
        try:
            self.client.delete('/simple/class/')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_get_with_query_string_request(self):
        try:
            self.client.get('/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_post_with_query_string_request(self):
        try:
            self.client.post('/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_put_with_query_string_request(self):
        try:
            self.client.put('/simple/class/with_query_string/?data=data', data={'data_json': 'data_json'}, content_type='application/json')
        except Exception as e:
            pytest.fail(f"Error: {e}")
    
    def test_middleware_simple_delete_with_query_string_request(self):
        try:
            self.client.delete('/simple/class/with_query_string/', {'data': 'data'})
        except Exception as e:
            pytest.fail(f"Error: {e}")