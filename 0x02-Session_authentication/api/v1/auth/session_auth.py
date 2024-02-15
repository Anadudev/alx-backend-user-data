#!/usr/bin/env python3
"""SessionAuth class"""
from uuid import uuid4
from api.v1.auth.auth import Auth
from models.user import User

class SessionAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if not (user_id and isinstance(user_id, str)):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return self.user_id_by_session_id.get(session_id, None)
    def current_user(self, request=None):
        """Gets the curent user based on session ID"""
        cookie =  self.session_cookie(request)
        if cookie:
            id = self.user_id_for_session_id(cookie)
            if id:
                return User.get(id)
        return None
