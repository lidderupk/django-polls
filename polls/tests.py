from django.test import TestCase
from polls.model import Poll
from django.utils import timezone

class PollMethodsTest(TestCase):
	def test_was_published_recently_with_future_poll(self):
			"""
			was published_recently() should return False for polls whose
			pub_date is in the future
			"""
			future_poll = Poll(pub_date = timezone.now() + datetime.timedelta(days=20))
			self.assertEqual(future_poll.was_published_recently(), False)