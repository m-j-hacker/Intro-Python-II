class NameStorage:
    def __init__(self, name, storage=[]):
        self.name = name
        self.storage = storage

    def add_item(item):
        self.storage.append(item)

    def remove_item(item):
        self.storage.pop(item)

class Description(NameStorage):
    def __init__(self, name, description, storage=[]):
        super().__init__(name, storage=storage)
        self.description = description

    def __str__(self):
        return f'Name: {self.name} \n Description: {self.description}\n '

    def __repr__(self):
        return f'Name: {self.name} \n Description: {self.description}\n '