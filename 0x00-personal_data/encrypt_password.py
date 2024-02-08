#!/usr/bin/env python3
""" Encrypting passwords """
import bcrypt


def hash_password(password: str):
    """_summary_

    Args:
        password (str): _description_

    Returns:
        _type_: _description_
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """_summary_

    Args:
        hashed_password (bytes): _description_
        password (str): _description_

    Returns:
        bool: _description_
    """
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    return False
