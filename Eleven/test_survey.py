#python3 test_survey.py

import unittest
from survey import AnonymousSurvey

class TestsAnonymousSurvey(unittest.TestCase):
	"""Tests for the AnonymousSurvey Class."""

	def setUp(self):
		"""Create a survey and a set of responses for use in all test methods."""
		question = "What was the first language you learned to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']
	
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

unittest.main()

#class TestsAnonymousSurvey(unittest.TestCase):
#	"""Tests for the AnonymousSurvey Class."""

#	def test_store_single_response(self):
#		"""Test that a single response is stored properly."""
#		question = "What was the first language you learned to speak?"
#		my_survey = AnonymousSurvey(question)
#		my_survey.store_response('English')

#		self.assertIn('English', my_survey.responses)

#	def test_store_three_responses(self):
#		"""Test that three individual responses are stored properly."""
#		question = "What was the first language  you learned to speak?"
#		my_survey = AnonymousSurvey(question)
#		responses = ['English', 'Spanish', 'Mandarin']
#		for response in responses:
#			my_survey.store_response(response)

#		for response in responses:
#			self.assertIn(response, my_survey.responses)

#unittest.main()
