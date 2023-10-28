from abc import ABC, abstractmethod

# Creation of abstract base class for custom views
class UserView(ABC):
    @abstractmethod
    def display(self):
        pass

class ConsoleUserView(UserView):
    def __init__(self, data):
        self.data = data

    def display(self):
        for record in self.data:
            print(record)

class WebView(UserView):
    def __init__(self, data):
        self.data = data

    def display(self):
        # Implementation of output in the web interface
        pass

class PersonalAssistant:
    def __init__(self):
        self.address_book = AddressBook()

    def add_record(self, record):
        self.address_book.add_record(record)

    def find_record(self, name):
        try:
            return self.address_book.find(name)
        except KeyError:
            return None

    def delete_record(self, name):
        try:
            self.address_book.delete(name)
        except KeyError:
            return 'No contact with this name'

    def display_records(self, view):
        view.display()