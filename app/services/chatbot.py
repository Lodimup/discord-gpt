import openai
from services.console import console


class ChatBot:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_hist=3):
        openai.api_key = api_key
        self.model = model
        self.messages = []
        self.max_hist = max_hist

    def _handle_max_hist(self) -> None:
        """
        Check if the message list is longer than the max history.
        If it is, remove the oldest message. that is not a system message.
        """
        if len(self.messages) > self.max_hist:
            self.messages.pop(1)
            self.messages.pop(1)

    def _is_system_exists(self) -> bool:
        """
        Check if there is a system message in the messages list.
        :return: True if there is a system message, False otherwise.
        """
        for i in self.messages:
            if i.get("role") == "system":
                return True

        return False

    def set_system_message(self, content: str) -> None:
        """
        Set the system message.
        if there is already a system message, it will be replaced,
        and the message list will be cleared.
        :param content: The content of the system message.
        """
        if self._is_system_exists():
            self.messages = []

        self.messages.append(
            {
                "role": "system",
                "content": content
            }
        )

    def chat(self, content: str) -> str:
        """
        Send a message to the chatbot and get a response.
        :param message: The message to send.
        :return: The response from the chatbot.
        """
        self.messages.append(
            {
                "role": "user",
                "content": content
            }
        )
        r = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        d_r = r.to_dict()['choices'][0]['message'].to_dict()
        self.messages.append({
            "role": d_r['role'],
            "content": d_r['content']
        })
        console.log(self.messages)
        self._handle_max_hist()

        return d_r['content']
