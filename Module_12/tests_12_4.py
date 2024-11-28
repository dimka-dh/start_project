import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            logging.warning(f"Тест {func.__name__} пропущен: Тесты в этом кейсе заморожены")
            return
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Бегун", speed=5)

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(123, speed=5)
            runner.run()
            self.assertEqual(runner.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("Бегун", speed=-1)
            runner.walk()
            self.assertEqual(runner.distance, 5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    @skip_if_frozen
    def test_challenge(self):
        try:
            self.runner.run()
            self.runner.walk()
            self.assertEqual(self.runner.distance, 15)
            logging.info('"test_challenge" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка в test_challenge: {e}")


if __name__ == "__main__":
    unittest.main()
