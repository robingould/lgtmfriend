import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv(override=True)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")

class GithubClient:
    def __init__(self):
        self.token = GITHUB_TOKEN
        self.client_id = GITHUB_CLIENT_ID
        self.headers = {
                        'Authorization': f'Bearer {self.token}',
                        'X-GitHub-Api-Version': '2022-11-28'
                        }
        self.session = requests.Session()
        self.session.headers.update({
                        'Authorization': f'Bearer {self.token}',
                        'X-GitHub-Api-Version': '2022-11-28'
                        })
        self.scope = 'repo:status'
        self.authorization_url = 'https://github.com/login/oauth/authorize?'

    def _sendRequest(self, url: str, params: dict = None) -> str | None:
        """
        Sends GET request to some url, with a dict of optional query parameters.
        """
        try:
            response = requests.get(url, params=urlencode(params))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Issue with response from request: {error}")
            return None
        
    def get_token(self) -> None:
        """Handle grant flow for client credentialization 
        """
        url = f"{self.authorization_url}client_id={self.client_id}&scope={self.scope}"
        post_result = self.session.post(url)
        self.access_token = post_result.json()['access_token']
        self.update_headers()
        
    def getOpenPullRequests(self, OWNER: str, repo: str) -> str | None:
        """
        Lists pull requests in a specified repository.
        This endpoint supports the following custom media types. For more information, see https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types

            application/vnd.github.raw+json: Returns the raw markdown body. Response will include body. This is the default if you do not pass any specific media type.
            application/vnd.github.text+json: Returns a text only representation of the markdown body. Response will include body_text.
            application/vnd.github.html+json: Returns HTML rendered from the body's markdown. Response will include body_html.
            application/vnd.github.full+json: Returns raw, text, and HTML representations. Response will include body, body_text, and body_html.

        cURL request looks like:
                curl -L \
                    -H "Accept: application/vnd.github+json" \
                    -H "Authorization: Bearer <YOUR-TOKEN>" \
                    -H "X-GitHub-Api-Version: 2022-11-28" \
                    https://api.github.com/repos/OWNER/REPO/pulls
       
        """
        pass
    