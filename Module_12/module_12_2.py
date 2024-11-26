import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        # Создаём участников
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print({place: str(runner) for place, runner in result.items()})

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.__class__.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
