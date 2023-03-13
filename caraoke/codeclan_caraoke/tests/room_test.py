import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("vocal point", 4)
        self.guest_2 = Guest("Jon")
        self.checked_in_guests = []
        self.song_1 = Song("how soon is now")
        self.song_2 = Song("bigmouth strikes again")
        self.song_3 = Song("this charming man")
        self.available_songs = {
            "The Smiths":[self.song_1, self.song_2, self.song_3]
        }
       
    def test_get_room_name(self):
        self.assertEqual("vocal point", self.room_1.get_room_name())

    def test_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(1, self.room_1.count_checked_guests())

    def test_can_remove_guest(self):
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.remove_guest(self.guest_2)
        self.assertEqual(0, self.room_1.count_checked_guests())

    def test_can_add_song_to_current_song(self):
        self.current_song_list = []
        self.room_1.play_song(self.song_2)
        self.assertEqual(1, len(self.room_1.get_playing_song()))

    # def test_can_get_playing_song(self):
    #     self.current_song_list = []
    #     self.room_1.play_song(self.song_2)
    #     # self.assertEqual("bigmouth strikes again", self.room_1.get_playing_song())
    #     self.assertEqual("bigmouth strikes again", self.current_song_list.get_song_title())

    def test_can_remove_song_from_list(self):
        self.current_song_list = []
        self.room_1.play_song(self.song_2)
        self.room_1.remove_song(self.song_2)
        self.assertEqual(0, len(self.room_1.get_playing_song()))
