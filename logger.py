import datetime
import threading
import pathlib
import os
from abc import ABC, abstractmethod
from log_strategy import LogStrategy
class Logger:
    """Класс, представляющий логгер для записи сообщений с различными уровнями важности."""

    _instance = None
    _file_lock = threading.Lock()
    _init_lock = threading.Lock()

    def __new__(cls):
        with cls._init_lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    """Записывает сообщение в файл с временной меткой и уровнем важности."""
    def _log(self, level: str, message: str, strategy: LogStrategy) -> None:
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}"
        strategy.log(log_message)

    def trace(self, message: str, strategy: LogStrategy) -> None:
        self._log("TRACE", message, strategy)

    def info(self, message: str, strategy: LogStrategy) -> None:
        self._log("INFO", message, strategy)

    def warn(self, message: str, strategy: LogStrategy) -> None:
        self._log("WARN", message, strategy)

    def error(self, message: str, strategy: LogStrategy) -> None:
        self._log("ERROR", message, strategy)

    def fatal(self, message: str, strategy: LogStrategy) -> None:
        self._log("FATAL", message, strategy)