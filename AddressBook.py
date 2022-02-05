import pickle

class AddressBook:
    """You can add/edit/remove contacts from address book"""

    __contacts = dict()
    __file_path = './storage/contacts.data'

    @staticmethod
    def add(name, email=None, phone=None):
        AddressBook.__contacts[name.lower()] = dict({
            'email': email,
            'phone': phone
        })

    @staticmethod
    def edit(name, email=None, phone=None):

        contact = AddressBook.__contacts[name.lower()]

        if email:
            contact['email'] = email
        if phone:
            contact['phone'] = phone

    @staticmethod
    def get(name):
        return AddressBook.__contacts[name.lower()]

    @staticmethod
    def delete(name):
        del AddressBook.__contacts[name.lower()]

    @staticmethod
    def all():
        return AddressBook.__contacts

    @staticmethod
    def drop():
        AddressBook.__contacts = dict()

    @staticmethod
    def dump():
        file = open(AddressBook.__file_path, 'wb')
        pickle.dump(AddressBook.__contacts, file)

    @staticmethod
    def load():
        file = open(AddressBook.__file_path, 'rb')
        AddressBook.__contacts = pickle.load(file)
