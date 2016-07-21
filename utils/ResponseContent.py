def getcontent(client, request):
    pathrequested = request.split('\n')[0]

    if 'GET / HTTP/1.1' in pathrequested or 'GET /index.html HTTP/1.1' in pathrequested \
            or 'GET / HTTP/1.0' in pathrequested or 'GET /index.html HTTP/1.0' in pathrequested:
        with open('files/index.html') as indexfile:
            index = indexfile.read()
            print('serving index.html')
            client.sendall(bytes(index, 'utf-8'))

    if 'GET /upload HTTP/1.1' in pathrequested or 'GET /upload.html HTTP/1.1' in pathrequested \
            or 'GET /upload HTTP/1.0' in pathrequested or 'GET /upload.html HTTP/1.0' in pathrequested:

        with open('files/upload.html') as uploadfile:
            upload = uploadfile.read()
            print('serving upload.html')
            client.sendall(bytes(upload, 'utf-8'))

    if \
            pathrequested.split(' ')[1].endswith('.jpg') or \
            pathrequested.split(' ')[1].endswith('.png') or \
            pathrequested.split(' ')[1].endswith('gif'):

        path = pathrequested.split(' ')[1]
        print(path)
        with open('files' + path, 'rb') as requestedfile:
            file = requestedfile.read()
            print(type(file))
            print(file)
            print('Serving image...')
            client.sendall(file)

    client.sendall('<html>'
                   '<head>'
                   '<title>Not found</title>'
                   '</head>'
                   '<body>'
                   '<h1>Content not found...</h1>'
                   '<br />'
                   '<h2>Wrong link?</h2>'
                   '</body>'
                   '</html>\n'.encode())
