# 23.contact_list.py

def load(csv):
    with open(csv) as file:
        lines = file.read().split('\n')

    contact_list = {}
    props = lines[0].split(',')
    for i in range(1, len(lines)):
        rows = lines[i].split(',')
        contact = dict(zip(props, rows))
        contact_list[contact['name']] = contact

    # for k, v in contact_list.items():
    #     print(k,v)

    return contact_list

def save(contact_list, props, name):
    contacts = [','.join(props)]
    for contact in contact_list:
        contact = contact_list[name]
        contacts.append(','.join(contact.values()))

    with open(csv, 'w') as f:
        f.write('\n'.join(contacts))

    return f'Savinf contacts as {csv}'

def create(contact_list, contact):

    if type(read(contact_list, contact[name])) is dict:
        return f'Error: {contact[name]} already exist.'
    contact_list[contact['name']] = contact
    return f'Created contact for {contact[name]}.'


def read(contact_list, name):

    return contact_list.get(name, f'Error: {name} not found')


def update(contact_list, name, updated_info):

    if contact_list.get(name):
        contact_list[name].update(updated_info)
        return f'Updated contact for {name}'
    return f'Error: {name} does not exist.'


def delete(contact_list, name):

    if contact_list.get(name):
        del contact_list[name]
        return f'{name} deleted'
    return f'Error: {name} does not exist'


def list_all(contact_list):
    for contact in contact_list:
        for k, v in contact_list[contact].items():
            print(f'{k}: {v}')


if __name__ == '__main__':
    contacts = load('contacts.csv')
    loop = True
    valid_input = ['c', 'r', 'u', 'd', 'e', 'x', 'h']
    commands: =
    '''
    Commands:
    (c)create
    (r)read
    (u)update
    (d)delete
    (e)xpand list
    e(x)it
    (h)elp
    '''

    print('Welcome to your contact list.')
    print(commands)
    while loop:
        while True:
            cmd = input('> ').strip().lower()
            if cmd in valid_input:
                break
            print('Invalid input.')
            print(commands)

        if cmd == 'x':
            #save contacts as csv
            print(save(contacts, 'contact_list.csv'))
            loop = False
            print('Goodbye')

        elif cmd in ['h', 'help']:
            print(commands)

        elif cmd.startswith('c'):
            contact = {}
            for props in props:
                contact[props] = input(f'{props}: ')
            print(create(contacts, contact))

        elif cmd.startswith('r'):
            name = input('Name: ')
            print(read(contacts, name))

        elif cmd.startswith('u'):
            name = input('name: ')
            contact = {}
            for prop in props:
                val = input(f'{prop}: ')
                if val:
                    contact[prop] = val
            print(update(contacts, name, contact))

        elif cmd.startswith('d'):
            name = input('Name: ')
            print(delete(contacts, name))

        elif cmd.startswith('e'):
            list_all(contacts)

        else:
            print(commands)
