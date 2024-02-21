#!/usr/bin/env python3
"""password hashing"""
import bcrypt
from user import User


def _hash_password(password: str) -> bytes:
    """ method that returns a hash password in bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        query = session.query(User).filter(User.email == email, User.password == password)
        if session.query(query.exists()).scalar():
            raise ValueError(f"User {email} already exists")
        else:
            _hash_password(password)
