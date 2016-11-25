from django.test import TestCase
from .models import Contact

# Create your tests here.
class ContactTest(TestCase):
    def test_str(self):
        test_mobile = Contact(mobile='TRY')
        self.assertEqual(str(test_mobile),
                         'TRY')






