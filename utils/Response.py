from utils import ResponseHeaders


def GetResponse(client, request, toSend):
    pathrequested = request.split('\n')[0]

    # if 'GET / HTTP/1.1' in pathrequested or 'GET /index.html HTTP/1.1' in pathrequested \
    #         or 'GET / HTTP/1.0' in pathrequested or 'GET /index.html HTTP/1.0' in pathrequested:
    #     with open('files/index.html') as indexfile:
    #         index = indexfile.read()
    #         print('serving index.html')
    #         if toSend:
    #             client.sendall(bytes(index, 'utf-8'))
    #         return index
    #
    # if 'GET /upload HTTP/1.1' in pathrequested or 'GET /upload.html HTTP/1.1' in pathrequested \
    #         or 'GET /upload HTTP/1.0' in pathrequested or 'GET /upload.html HTTP/1.0' in pathrequested:
    #     with open('files/upload.html') as uploadfile:
    #         upload = uploadfile.read()
    #         print('serving upload.html')
    #         if toSend:
    #             client.sendall(bytes(upload, 'utf-8'))
    #         return upload
    exactpath = pathrequested.split(' ')[1]
    if exactpath == '/':
        with open('files/index.html') as indexfile:
            index = indexfile.read()
            ResponseHeaders.ResponseCodes.Send200Response(client, 'text/html', index)
            client.sendall(index.encode('utf-8'))
        return
    try:
        with open('files' + exactpath, 'rb') as requestedresource:
            resource = requestedresource.read()
            if exactpath.endswith('.jpg'):
                ResponseHeaders.ResponseCodes.Send200Response(client, 'image/jpeg', resource)
            elif exactpath.endswith('.png'):
                ResponseHeaders.ResponseCodes.Send200Response(client, 'image/png', resource)
            elif exactpath.endswith('.gif'):
                ResponseHeaders.ResponseCodes.Send200Response(client, 'image/gif', resource)
            elif exactpath.endswith('.css'):
                ResponseHeaders.ResponseCodes.Send200Response(client, 'text/css', resource)
            else:
                ResponseHeaders.ResponseCodes.Send200Response(client, 'text/html', resource)
            client.sendall(resource)
            return

    except (OSError, IOError, IsADirectoryError):
        try:
            with open('files' + exactpath + '.html', 'rb') as requestedfailsource:
                resourcefail = requestedfailsource.read()
                ResponseHeaders.ResponseCodes.Send200Response(client, 'text/html', resourcefail)
                client.sendall(resourcefail)
        except (OSError, IOError, IsADirectoryError):
            pass
        ResponseHeaders.ResponseCodes.Send404Response(client, 'text/html', get404page())
        print(get404page())
        client.sendall(get404page())



def get404page():
    with open('files/404.html') as file404:
        notfound = file404.read()
        return notfound.encode('utf-8')
