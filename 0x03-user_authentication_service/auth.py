#!/usr/bin/env python3
"""password hashing"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ method that returns a hash password in bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
