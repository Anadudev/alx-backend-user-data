#!/usr/bin/env python3
""" regexing """
import os
import re
import logging
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields, redaction, message, separator):
    for i in fields:
        message = re.sub(f"{i}=.*?{separator}", f"{i}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """_summary_

    Returns:
        logging.Logger: _description_
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """_summary_

    Returns:
        mysql.connector.connection.MySQLConnection: _description_
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "localhost")
    database = os.getenv(
        "PERSONAL_DATA_DB_NAME",
    )

    my_db = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )

    return my_db


def main():
    """_summary_"""
    my_db = get_db()
    logger = get_logger()
    cursor = my_db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = cursor.column_names
    for row in cursor:
        data_row = "".join(f"{f}={str(r)}; " for r, f in zip(row, field_names))
        logger.info(data_row.strip())
    cursor.close()
    my_db.close()


if __name__ == "__main__":
    main()
