from unicodedata import category
from django.test import TestCase

from books.models import Category, Book, Author

# Create your tests here.

class CategoryModelTest(TestCase):
  """
  test for category model
  """
  def setUp(self):
    """
    Set up non modified object used by all test methods.
    """
    Category.objects.create(name='test', description='test', status=True)
  
  def test_category_name_is_not_blank(self):
    """
    test for category name is not blank
    """
    category = Category.objects.get(id=1)
    self.assertEqual(category.name, 'test')