import unittest
from unittest.mock import MagicMock, patch
import io
from LR2 import Logger, ConsoleLogStrategy, FileLogStrategy, UpperFileLogStrategy


class TestLogger(unittest.TestCase):

    def setUp(self):
        """ Создаем экземпляр Logger перед каждым тестом"""
        self.logger = Logger()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_logging(self, mock_stdout):
        """ Тестируем логирование в консоль"""
        strategy = ConsoleLogStrategy()
        self.logger.info("Тестовое сообщение в консоль", strategy)

        output = mock_stdout.getvalue()

        self.assertIn("INFO", output)
        self.assertIn("Тестовое сообщение в консоль", output)

        def test_file_logging(self):
            """ Тестируем логирование в файл """

        with patch('builtins.open', new_callable=MagicMock) as mock_open:
            mock_file = MagicMock()
            # Настраиваем mock для файла
            mock_open.return_value.__enter__.return_value = mock_file

            strategy = FileLogStrategy('dummy_path.log')
            self.logger.error("Тестовое ошибочное сообщение", strategy)

            # Проверяем, что open был вызван с правильным аргументом
            mock_open.assert_called_once_with('dummy_path.log', 'a', encoding='utf-8')
            # Проверяем, что write был вызван
            mock_file.write.assert_called()
            # Получаем последнее записанное сообщение
            written_message = mock_file.write.call_args[0][0]
            self.assertIn("ERROR", written_message)
            self.assertIn("Тестовое ошибочное сообщение", written_message)

    def test_upper_file_logging(self):
        """ Тестируем логирование в файл в верхнем регистре"""
        with patch('builtins.open', new_callable=MagicMock) as mock_open:
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            strategy = UpperFileLogStrategy('dummy_path.log')
            self.logger.info("Тестовое сообщение с ошибкой", strategy)

            mock_open.assert_called_once_with('dummy_path.log', 'a', encoding='utf-8')
            mock_file.write.assert_called()
            written_message = mock_file.write.call_args[0][0]
            self.assertIn("INFO", written_message)
            self.assertIn("ТЕСТОВОЕ СООБЩЕНИЕ С ОШИБКОЙ", written_message)


if __name__ == '__main__':
    unittest.main()
