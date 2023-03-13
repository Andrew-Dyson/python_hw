import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("how soon is now?")

    def test_song_has_a_title(self):
        self.assertEqual("how soon is now?", self.song_1.get_song_title())