from urllib.parse import urljoin, urlencode
import requests
import pkce
from http import HTTPStatus


class User:
    session: requests.Session

    def __init__(self):
        self.base_url = 'http://127.0.0.1:9000'
        self.session = requests.session()

    def pre_request(self):
        code_verifier = pkce.generate_code_verifier(length=43)
        code_challenge = pkce.get_code_challenge(code_verifier)
        code_challenge_method = pkce.get_code_challenge(code_verifier)

        self.session.get(urljoin(self.base_url, "/oauth2/authorize"), params=dict(
            response_type='code',
            client_id='client',
            scope='openid',
            redirect_uri='http://127.0.0.1:3000/authorized',
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method
        ))

    # doesn't work
    def login(self):
        _csrf = self.session.cookies.get('XSRF-TOKEN')
        response = self.session.post(urljoin(self.base_url, "/login"), params=urlencode(dict(
            _csrf=_csrf,
            username='test',
            password='12345'
        )))


    def register(self, user: str, password: str):
        self.pre_request()
        _csrf = self.session.cookies.get('XSRF-TOKEN')
        response = self.session.post(urljoin(self.base_url, "/register"), params=urlencode(dict(
            _csrf=_csrf,
            username=user,
            password=password,
            passwordSubmit=password
        )))

        if response.status_code == HTTPStatus.CREATED:
            return 'created'
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            return 'already exists'
        else:
            raise f'Error: response status {response.status_code}'

