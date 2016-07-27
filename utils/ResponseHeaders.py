from utils import logger

__servername__ = 'PythonServer/1.0'


def getReferer(request):
    refererheader = None
    headers = request.split('\n')
    for header in headers:
        if 'Referer: ' in header:
            refererheader = header
            break

    if refererheader is None:
        return False

    referer = refererheader.split(' ')[1]
    return referer


def getcontentlenght(resource):
    return len(resource)


class ResponseCodes:
    @staticmethod
    def Send200Response(client, contenttype, content):
        response = 'HTTP/1.0 200 OK\n'\
                   'Server: {0}\n'\
                   'Content-Type: {1}\n' \
                   'Content-Length: {2}'\
                   '\r\n\r\n'.format(__servername__, contenttype, len(content)).encode()
        client.sendall(response)
        logger.logaccess(response.decode())
        return response

    @staticmethod
    def Send404Response(client, contenttype, content):
        response = 'HTTP/1.0 404 Not Found\n' \
                   'Server: {0}\n' \
                   'Content-Type: {1}\n' \
                   'Content-Length: {2}\n' \
                   '\r\n\r\n'.format(__servername__, contenttype, len(content)).encode()
        client.sendall(response)
        logger.logaccess(response.decode())
        return response

    @staticmethod
    def Send403Response(client, contenttype, content):
        response = 'HTTP/1.0 403 Forbidden\n' \
                              'Server: {0}\n' \
                              'Content-Type: {1}\n' \
                              'Content-Length: {2}\n' \
                              '\r\n\r\n'.format(__servername__, contenttype, len(content)).encode()
        client.sendall(response)
        logger.logaccess(response.decode())
        return response

    @staticmethod
    def Send500Response(client, contenttype, content):
        response = 'HTTP/1.0 500 Internal Server Error\n' \
                       'Server: {0}\n' \
                       'Content-Type: {1}\n' \
                       'Content-Length: {2}\n' \
                       '\r\n\r\n'.format(__servername__, contenttype, len(content)).encode()
        client.sendall(response)
        logger.logaccess(response.decode())
        return response
