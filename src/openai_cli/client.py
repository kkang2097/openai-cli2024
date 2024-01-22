import requests


class CompletionClient:
    MAX_TOKENS = 1000
    TEMPERATURE = 0.1
    TIMEOUT = 60

    def __init__(self, token: str, session: requests.Session, api_url: str) -> None:
        self._headers = {"Authorization": f"Bearer {token}"}
        self._session = session
        self._api_url = api_url

    def generate_response(self, prompt: str, model: str) -> str:
        """Generates response from a given prompt using a specified model.

        Args:
            prompt: The prompt to generate a response for.
            model: The model to use for generating the response.
                   Defaults to "text-davinci-003".

        Returns:
            The generated response.
        """
        json_data = {
    'model': f'{model}',
    'messages': [
        {
            'role': 'user',
                    'content': prompt,
        },
    ],
    }
        response = self._session.post(
            'https://api.openai.com/v1/chat/completions', headers=self._headers, json=json_data
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()


def build_completion_client(token: str, api_url: str) -> CompletionClient:
    return CompletionClient(token=token, session=requests.Session(), api_url=api_url)
