import unittest
from unittest.mock import MagicMock
from LR2 import Logger, ConsoleLogStrategy

class TestLogger(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.strategy = ConsoleLogStrategy()
        self.logger1 = Logger.get_instance(self.strategy)
        self.logger2 = Logger.get_instance(self.strategy)

    def test_logger_singleton(self):
        """Проверяем, что оба экземпляра логгера одинаковы."""
        self.assertIs(self.logger1, self.logger2)

    def test_logging_methods(self):
        """Проверяем, что методы логирования вызывают правильные функции."""
        self.logger1.log = MagicMock()

        # Тестируем метод info
        self.logger1.info("Тестовое сообщение")
        self.logger1.log.assert_called_with("INFO", "Тестовое сообщение")


        self.logger1.error("Ошибка")
        self.logger1.log.assert_called_with("ERROR", "Ошибка")

if __name__ == '__main__':
    unittest.main()