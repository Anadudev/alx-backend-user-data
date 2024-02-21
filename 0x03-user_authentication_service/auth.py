#!/usr/bin/env python3
"""password hashing"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ method that returns a hash password in bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method that handles user registration"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user
        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Method that validate suser login"""
        """try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hash_password)
        except NoResultFound:
            return False"""
        user = self._db.find_user_by(email=email)
        if user:
            return bcrypt.checkpw(password.encode(), user.hash_password)
        return False
