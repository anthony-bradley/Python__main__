#python3 language_survey.py

from survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What was the first language you learned to speak? "
my_survey = AnonymousSurvey(question)

#Show the question, and store responses to the question.
my_survey.show_question()
print("(Enter 'q' at any time to exit the prompt.)\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#Show the results of the survey.
print("\nThank you for participating in the survey!")
my_survey.show_results()