class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        if message not in self.lookup:
            self.lookup[message] = timestamp
            return True
        else:
            tmp = self.lookup[message]
            if timestamp - tmp < 10:
                return False
            else:
                self.lookup[message] = timestamp
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
