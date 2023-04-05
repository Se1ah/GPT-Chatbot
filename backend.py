import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=2000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)
