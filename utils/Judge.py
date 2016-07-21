from utils import ResponseHeaders
from utils import ResponseContent
from utils import logger


class Judge(object):

    def __init__(self, client, userrequest):
        self.client = client
        self.userrequest = userrequest

    def getjudgement(self):
        path = self.userrequest.split(' ')[1]
        pathrequested = self.userrequest.split('\n')[0]
        if \
                'GET / HTTP/1.1' in pathrequested or 'GET /index.html HTTP/1.1' in pathrequested \
                or 'GET / HTTP/1.0' in pathrequested or 'GET /index.html HTTP/1.0' in pathrequested \
                or 'GET /upload HTTP/1.1' in pathrequested or 'GET /upload.html HTTP/1.1' in pathrequested \
                or 'GET /upload HTTP/1.0' in pathrequested or 'GET /upload.html HTTP/1.0' in pathrequested:

            response = ResponseHeaders.Send200Response(self.client, self.userrequest)
            content = ResponseContent.getcontent(self.client, self.userrequest)
            return

        elif path.endswith('jpg'):
            ResponseHeaders.Send200Response(self.client, 'image/jpg')
            ResponseContent.getcontent(self.client, self.userrequest)
            return
        elif path.endswith('.png'):
            ResponseHeaders.Send200Response(self.client, 'image/png')
            ResponseContent.getcontent(self.client, self.userrequest)
            return

        ResponseHeaders.Send404Response(self.client, 'text/html')
        return ResponseContent.getcontent(self.client, self.userrequest)


