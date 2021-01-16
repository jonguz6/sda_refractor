from datetime import datetime
import time


class Logger:
    class __Singleton:
        def __init__(self, file_name):
            self._file_name = file_name

        def log(self, log_msg):
            with open(self._file_name, 'a') as f:
                f.write(f"{datetime.now()} - {log_msg}\n")

    __instance = None

    def __new__(cls, file_name):
        if not Logger.__instance:
            Logger.__instance = Logger.__Singleton(file_name)
        return Logger.__instance


if __name__ == "__main__":
    one = Logger("log.txt")
    one.log("one")
    one.log("two")
    time.sleep(1)
    one.log("three")