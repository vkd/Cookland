from django.test import TestCase
from cookland.models import CookPost

class CookPostTestCase(TestCase):
	def setUp(self):
		CookPost.objects.create(id=1,
			title='first',
			body='first_body')
		CookPost.objects.create(id=2,
			title='second',
			body='second_body')

	def test_posts_have_category(self):
		first_post = CookPost.objects.get(id=1)
		second_post = CookPost.objects.get(id=2)

		self.assertEqual(first_post.title, 'first')
		self.assertEqual(second_post.title, 'second')