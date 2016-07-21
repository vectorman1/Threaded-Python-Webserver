def logaccess(arg):
    with open('logs/access.log', 'a') as accesslog:
        accesslog.write(arg)

    print('Access logged.')


def logerror(arg):
    with open('logs/error.log', 'a') as errorlog:
        errorlog.write(arg)

    print('Error logged.')