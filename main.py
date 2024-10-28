import os
from log_strategy import FileLogStrategy, ConsoleLogStrategy, UpperFileLogStrategy
from logger import Logger
import datetime
import threading
import pathlib
import os

def main():
    save_folder_path = os.getcwd()
    log_file_name = f"DP.P1.{datetime.datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.log"
    log_file_path = pathlib.Path(save_folder_path) / log_file_name

    logger = Logger()

    # Логирую в файл в нижнем регистре
    file_strategy = FileLogStrategy(log_file_path)
    logger.trace("Начало работы программы", file_strategy)
    logger.info("Программа запущена успешно", file_strategy)

    # Логирование в консоль
    console_strategy = ConsoleLogStrategy()
    logger.warn("возможно проблемы", console_strategy)
    logger.error("Ошибка ", console_strategy)
    logger.fatal("Фатальная ошибка", console_strategy)

    # Логирую в верхнем регистре
    upper_file_strategy = UpperFileLogStrategy(log_file_path)
    logger.info("Сообщение для верхнего регистра", upper_file_strategy)


if __name__ == "__main__":
    main()
