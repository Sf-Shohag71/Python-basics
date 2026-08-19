import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    
    question = "What is your first ever learning programming language?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response stored properly"""

    language_survey.store_response("Python")
    assert 'Python' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three responses are stored properly"""

    responses = ['English', 'Bengali', 'Science']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses