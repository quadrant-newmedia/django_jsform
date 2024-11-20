from django.test import TestCase


class MyTestCase(TestCase):
    def test_imports_cleanly(self):
        from django_jsform import js_response
        from django_jsform.templatetags import jsform
