from iugu_exceptions import IuguAuthenticationException, IuguObjectNotFound
from iugu import Iugu
import base64
import json
from utilities import Utilities

class APIRequest:

    def __defaultHeaders(self, headers = []):
        headers.append("Authorization: Basic " + base64.b64encode(Iugu.getApiKey() + ":"))
        headers.append("Accept: application/json")
        headers.append("Accept-Charset: utf-8")
        headers.append("User-Agent: Iugu PHPLibrary")
        headers.append("Accept-Language: pt-br;q=0.9,pt-BR")
        return headers

    def request(self, method, url, data=[]):
        if Iugu.getApiKey() is None:
            Utilities.authFromEnv()

        if Iugu.getApiKey() is None:
            raise IuguAuthenticationException("Chave de API não configurada. Utilize Iugu.setApiKey(...) para configurar.")

        headers = self.__defaultHeaders()
        ( response_body, response_code ) = self._requestWithCURL( method, url, headers, data )
        try:
            response = json.loads(response_body)
        except ValueError:
            raise IuguObjectNotFound(response_body)

        if response_code == 404:
            raise IuguObjectNotFound(response_body)

        if response.errors is not None:
            if type(response.errors) != "str" and len(response.errors) == 0:
                response.errors = None
            elif type(response.errors) != "str" and len(response.errors) > 0:
                response.errors = response.errors
            if response.errors is not None and type(response.errors) == "str":
                response.errors = response.errors
        iugu_last_api_response_code = response_code
        return response

    def _requestWithCURL(self, method, url, headers, data=[]):
        pass
