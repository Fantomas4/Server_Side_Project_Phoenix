import unittest
import Project_Phoenix as phoenix

class PhoenixTestCase(unittest.TestCase):
    def setUp(self):
        phoenix.app.config['TESTING'] = True
        self.app = phoenix.app.test_client()

    def test_song_count(self):
        rv = self.app.get('/song_count/set/44')
        assert b'OK' in rv.data
        rv = self.app.get('/song_count/get')
        assert b'44' in rv.data


if __name__ == '__main__':
    unittest.main()