import unittest
import Project_Phoenix as phoenix

class PhoenixTestCase(unittest.TestCase):
    def setUp(self):
        phoenix.app.config['TESTING'] = True
        self.app = phoenix.app.test_client()

    def __assert_ok(self, url):
        rv = self.app.get(url)
        assert b'OK' in rv.data

    def test_song_count(self):
        rv = self.app.get('/song_count/set/44')
        assert b'OK' in rv.data
        rv = self.app.get('/song_count/get')
        assert b'44' in rv.data

    def test_vote_result(self):
        self.__assert_ok('/song_count/set/50')
        for i in range(0,10):
            self.__assert_ok('/vote/record/25')
        for i in range(0,25):
            self.__assert_ok('/vote/record/14')
        for i in range(0,24):
            self.__assert_ok('/vote/record/47')

        rv = self.app.get('/vote/result')
        assert b'14' in rv.data


if __name__ == '__main__':
    unittest.main()