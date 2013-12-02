from django.test import TestCase
from selenium import webdriver
from django.test import LiveServerTestCase

class PollsTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


	def test_can_create_new_poll_via_admin_site(self):
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)
		self.fail('finish this test')