import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently(self):
        print("testing")
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), True)

    def test_was_df(self):
        """
        was published recently returns False for question which pub_date
        is in the future.
        """
        print("testing2")
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

# class Footest(TestCase):
#     def setUp(self):
#         pass
#
#     def testDown(self):
#         pass
#
#     def this_wont_run(self):
#         print("Failed")
#
#     def test_this_will(self):
#         print("Win")
