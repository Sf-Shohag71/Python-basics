from survey import AnonymousSurvey

# Define question for language survey
question = "What is your first ever learning programming language?"
language_survey = AnonymousSurvey(question)
language_survey.show_question()

# Store responses to a list
while True:
    response = input("Enter programming language name(type 'q' for quit): ")
    if response.lower() == 'q':
        break

    # Store responses
    language_survey.store_response(response)

# Show responses 
print("\nThank you everyone who participated to the survey.")
language_survey.show_result()