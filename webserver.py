import linecache
import socket
import threading
import sys

from utils import logger
from utils.Judge import Judge


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(1)
            try:
                threading.Thread(target=self.listenToClient, args=(client, address)).start()
            except Exception as e:
                exc_type, exc_obj, tb = sys.exc_info()
                f = tb.tb_frame
                lineno = tb.tb_lineno
                filename = f.f_code.co_filename
                linecache.checkcache(filename)
                line = linecache.getline(filename, lineno, f.f_globals)

                error = 'EXCEPTION IN ({}, LINE {} "{}"): {}\n'.format(filename, lineno, line.strip(), exc_obj)

                logger.logerror(error)

    def listenToClient(self, client, address):
        data = client.recv(1024)
        while True:
            try:
                if data:
                    judge = Judge(client, data.decode())
                    judge.getjudgement()
                    logger.logaccess(data.decode())
                    logger.logaccess('-----------\n')
                    break
                else:
                    logger.logerror('Client Disconnected')
                    raise socket.error('Client disconnected')

            except Exception as ex:
                print(sys.stderr())
                exc_type, exc_obj, tb = sys.exc_info()
                f = tb.tb_frame
                lineno = tb.tb_lineno
                filename = f.f_code.co_filename
                linecache.checkcache(filename)
                line = linecache.getline(filename, lineno, f.f_globals)

                error = 'EXCEPTION IN ({}, LINE {} "{}"): {}\n'.format(filename, lineno, line.strip(), exc_obj)

                logger.logerror(error)

                client.close()
                return False
        client.close()


if __name__ == "__main__":
    print('PythonServer initialized at port 8080...\nListening...')
    ThreadedServer('',8080).listen()
