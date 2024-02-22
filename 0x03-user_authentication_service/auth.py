#!/usr/bin/env python3
"""password hashing"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ method that returns a hash password in bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """method that return a string representation of a new UUID"""
    return str(uuid4())


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
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """a method that generates a user session"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ returns the corresponding User or None"""
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """mwthod that desgroys a user session"""
        try:
            user = _db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        user.session_id = None
        return None
