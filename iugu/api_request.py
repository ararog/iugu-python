

class APIRequest:

    def __defaultHeaders(self, headers = []):
        headers.append("Authorization: Basic " . base64_encode(Iugu.getApiKey() + ":"))
        headers.append("Accept: application/json")
        headers.append("Accept-Charset: utf-8")
        headers.append("User-Agent: Iugu PHPLibrary")
        headers.append("Accept-Language: pt-br;q=0.9,pt-BR")
        return headers

    def request(self, method, url, data=[]):
        if Iugu.getApiKey() is None:
            Iugu_Utilities.authFromEnv()

        if Iugu.getApiKey() is None:
            raise IuguAuthenticationException("Chave de API não configurada. Utilize Iugu.setApiKey(...) para configurar.")

        headers = self._defaultHeaders()
        list( response_body, response_code ) = self.requestWithCURL( method, url, headers, data )
        response = json_decode(response_body)

        if json_last_error() != JSON_ERROR_NONE:
            raise IuguObjectNotFound(response_body)

        if response_code == 404:
            raise IuguObjectNotFound(response_body)

        if response.errors is not None:
            if gettype(response.errors) != "string" and count(get_object_vars(response.errors)) == 0:
                unset(response.errors)
            else if gettype(response.errors) != "string" and count(get_object_vars(response.errors)) > 0:
                response.errors = (Array) response.errors
            if isset(response.errors and gettype(response.errors) == "string"):
                response.errors = response.errors
        iugu_last_api_response_code = response_code
        return response
