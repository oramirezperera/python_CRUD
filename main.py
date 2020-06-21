clients = 'Pablo, Ricardo,'

def create_client(client_name):
    global clients   #you add the global clients so you can acces the clients global variable

    clients += client_name
    _add_comma()


def list_clients():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients += ','


if __name__ == '__main__':
    list_clients()

    create_client('David')

    list_clients()
