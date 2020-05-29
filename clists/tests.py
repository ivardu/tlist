from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


# Testcase for the list of the clists url's
class ClistURLTest(TestCase):

	def setUp(self):
		pass
	# Landing page url test
	def test_lp_url(self):
		lp_url = self.client.get(reverse('land_page'))
		self.assertEqual(lp_url.status_code, 300)
	# create url page test
	def test_create_url(self):
		create_url = self.client.get(reverse('create'))
		self.assertEqual(create_url.status_code, 300)
	# My Checklist page url test
	def test_myclists_url(self):
		mycl_url = self.client.get(reverse('myclists'))
		self.assertEqual(mycl_url.status_code, 300)
