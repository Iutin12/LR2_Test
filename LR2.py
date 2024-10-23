import datetime
import threading


# Определяем интерфейс стратегии для логирования
class LogStrategy:
    def log(self, message):
        raise NotImplementedError("Метод log должен быть реализован в подклассах")


# Реализация стратегии для записи в консоль
class ConsoleLogStrategy(LogStrategy):
    def log(self, message):
        print(message)


# Реализация стратегии для записи в файл
class FileLogStrategy(LogStrategy):
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = threading.Lock()
        self.open_file()

    def open_file(self):
        with self.lock:
            self.file = open(self.file_name, 'w', encoding='utf-8')

    def log(self, message):
        with self.lock:
            self.file.write(message + '\n')


    def close(self):
        with self.lock:
            self.file.close()


# Реализация стратегии для записи в файл в верхнем регистре
class UpperCaseFileLogStrategy(FileLogStrategy):
    def log(self, message):
        upper_message = message.upper()
        super().log(upper_message)


class Logger:
    """
    Логгер, который записывает сообщения различными способами.
    Использует шаблон Singleton, чтобы создать только один экземпляр логгера.
    """

    instance = None

    def __init__(self, strategy: LogStrategy):
        if Logger.instance is not None:
            raise Exception("Экземпляр уже создан")

        Logger.instance = self
        self.lock = threading.Lock()
        self.strategy = strategy

    @staticmethod
    def get_instance(strategy: LogStrategy):
        if Logger.instance is None:
            Logger(strategy)
        return Logger.instance

    def log(self, level, message):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}"

        with self.lock:
            self.strategy.log(log_message)

    def trace(self, message):
        self.log("TRACE", message)

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)

    def fatal(self, message):
        self.log("FATAL", message)


# Пример использования
if __name__ == "__main__":
    # Выбор стратегии логирования
    strategy_choice = input("Выберите стратегию логирования (console/file/uppercase_file): ").strip().lower()

    if strategy_choice == "console":
        strategy = ConsoleLogStrategy()
    elif strategy_choice == "file":
        file_name = f"DP.P1.{datetime.datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.log"
        strategy = FileLogStrategy(file_name)
    elif strategy_choice == "uppercase_file":
        file_name = f"DP.P1.{datetime.datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.log"
        strategy = UpperCaseFileLogStrategy(file_name)
    else:
        print("Неверный выбор стратегии. Используется консоль по умолчанию.")
        strategy = ConsoleLogStrategy()

    logger = Logger.get_instance(strategy)

    # Записываем разные сообщения в лог
    logger.trace("Начало работы программы")
    logger.info("Программа запущена успешно")
    logger.warn("Возможны проблемы с соединением с базой данных")
    logger.error("Ошибка выполнения операции")
    logger.fatal("Критическая ошибка, программа завершается")

