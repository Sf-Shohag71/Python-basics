class AnonymousSurvey:
    """Collect anonymous survey responses"""
    def __init__(self, question):
        """Store questions and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey questions"""
        print(self.question)

    def store_response(self, new_response):
        """Store survey responses"""
        self.responses.append(new_response)

    def show_result(self):
        print("Survey result: ")
        for response in self.responses:
            print(f"- {response}")