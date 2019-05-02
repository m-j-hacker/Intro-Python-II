# Write a class to hold player information, e.g. what room they are in
# currently.
from lib import NameStorage

class Player(NameStorage):
    def __init__(self, name, room, storage=[]):
        super().__init__(name, storage=storage)
        self.room = room
    
    def change_room(self, new_room):
        self.room = new_room