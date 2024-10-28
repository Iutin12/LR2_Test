import datetime
import threading
import pathlib
import os
from abc import ABC, abstractmethod

"""Абстрактный класс"""
class LogStrategy(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


"""Стратегия для вывода в консоли"""
class ConsoleLogStrategy(LogStrategy):
    def log(self, message: str) -> None:
        print(message)


"""Стратегия для вывода в файл"""
class FileLogStrategy(LogStrategy):
    def __init__(self, file_path: pathlib.Path):
        self.file_path = file_path

    def log(self, message: str) -> None:
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')


"""Стратегия для вывода в файл капслоком"""
class UpperFileLogStrategy(FileLogStrategy):
    def log(self, message: str) -> None:
        super().log(message.upper())
