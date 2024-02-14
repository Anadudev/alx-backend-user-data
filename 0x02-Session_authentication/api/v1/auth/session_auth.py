#!/usr/bin/env python3
"""Auth class"""
# import base64
from api.v1.auth.auth import Auth
# from typing import TypeVar
# from models.user import User
from uuid import uuid4

class SessionAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if not(user_id and isinstance(user_id, str)):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    def user_id_for_session_id(self, session_id: str = None) -> str:
            return self.user_id_by_session_id.get(session_id,None )
