import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }
]


def create_client(client):
    global clients   #you add the global clients so you can acces the clients global variable

    if client not in clients:
        clients.append(client)
    else:
        print('Client already exist')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')
        

def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
       if idx == client_id:
           del clients[idx]
           break


def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('Welcome to Platzi sales')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}?')

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')
    
        if client_name == 'exit':
            client_name == None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    
    return client


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client {client_name} is not in our client\'s list')
    elif command == 'L':
        list_clients()
    else:
        print('invalid command')
