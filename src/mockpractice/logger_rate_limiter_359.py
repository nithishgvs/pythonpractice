class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logs:
            if timestamp < self.logs[message]:
                return False
        self.logs[message] = 10 + timestamp
        return True

def test():
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(3, "foo"))
    print(logger.shouldPrintMessage(8, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))
