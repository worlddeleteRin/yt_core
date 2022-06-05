from httpx import Client, Response
from yt_core.models import *

class HttpModule():
    is_debug: bool = True
    client: Client 

    def __init__(
        self,
        client: Client
    ):
        self.client = client

    def process_response (
        self,
        response: Response
    ) -> BaseYtResponse:
        response_dict = dict(response.json())
        if response.status_code != 200:
            response_error = response_dict.get('error')
            if isinstance(response_error, dict):
                error = BaseYtErrorException(
                    response = response,
                    **response_error 
                )
            else:
                error = BaseYtErrorException.get_dummy_from_response(
                    response
                )
            raise error
        # response_success = response_dict.get('response')
        if ( 
            'error' in response_dict or
            'error_code' in response_dict
        ):
            raise BaseYtErrorException.get_dummy_from_response(
                response
            )
        return BaseYtResponse(
            response = response 
        )

class YtClient:
    http: HttpModule

    def __init__(self):
        self.http = HttpModule(
            client = Client(
                base_url = '',
                params = {
                    # 'access_token': '',
                    # 'application_key': ''
                }
            )
        )
