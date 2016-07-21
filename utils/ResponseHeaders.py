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


def Send200Response(client, contenttype):
    response = 'HTTP/1.0 200 OK\n'\
               'Server: {0}\n'\
               'Content-Type: {1}\n'\
               '\r\n\r\n'.format(__servername__, contenttype).encode()
    client.sendall(response)
    return response


def Send404Response(client, contenttype):
    response = 'HTTP/1.0 Not Found\n' \
               'Server: {0}\n' \
               'Content-Type: {1}\n' \
               '\r\n\r\n'.format(__servername__, contenttype).encode()
    client.sendall(response)
    return response


def Send403Response(client, contenttype):
    return client.sendall('HTTP/1.0 403 Forbidden\n'
                          'Server: {0}\n'
                          'Content-Type: {1}\n'
                          '\r\n\r\n'.format(__servername__, contenttype).encode())


def Send500Response(client, contenttype):
    client.sendall('HTTP/1.0 500 Internal Server Error\n'
                   'Server: {0}\n'
                   'Content-Type: {1}\n'
                   '\r\n\r\n'.format(__servername__, contenttype).encode())
