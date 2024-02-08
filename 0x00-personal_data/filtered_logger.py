#!/usr/bin/env python3
""" regexing """
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields, redaction, message, separator):
    for i in fields:
        message = re.sub(f"{i}=.*?{separator}", f"{i}={redaction}{separator}", message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
         record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
         return super(RedactingFormatter,self).format(record)
def get_logger():
    logger = logging.getLogger("user_data")
    logegr.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StremHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
# if __name__="__main__":
