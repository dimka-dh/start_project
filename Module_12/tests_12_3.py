import unittest
from runner_and_tournament import Runner, Tournament


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Бегун", speed=5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @skip_if_frozen
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.nick = Runner("Ник", speed=3)
        self.tournament = Tournament(90, self.usain, self.nick)

    @skip_if_frozen
    def test_first_tournament(self):
        result = self.tournament.start()
        self.assertEqual(result[2].name, "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        self.tournament.participants.append(Runner("Андрей", speed=9))
        result = self.tournament.start()
        self.assertEqual(result[3].name, "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        result = self.tournament.start()
        self.assertTrue("Усэйн" in [r.name for r in result.values()])


if __name__ == "__main__":
    unittest.main()
