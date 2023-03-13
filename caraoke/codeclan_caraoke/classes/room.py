class Room:
    def __init__ (self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.checked_in_guests = []
        self.available_songs = {}
        self.current_song = []

    def get_room_name(self):
        return self.name 

    def check_in_guest(self, guest):
        self.checked_in_guests.append(guest)

    def count_checked_guests(self):
        return len(self.checked_in_guests)
        
    def remove_guest(self, guest):
        self.checked_in_guests.remove(guest)

    def get_playing_song(self):
        return self.current_song
        
    def play_song(self, song):
        self.current_song.append(song)

    def remove_song(self, song):
        self.current_song.remove(song)