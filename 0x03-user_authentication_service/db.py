#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import TypeVar

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Memoized session object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Method to find the first result of user information
        """
        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise InvalidRequestError
            resObject = self.__session.query(User)\
                .filter_by(**kwargs)\
                .first()
            if not resObject:
                raise NoResultFound
            return resObject

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Method to find the first result of user information
        """
        userResult = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in userResult.__table__.columns.keys():
                raise ValueError
            else:
                # userResult.key = value
                setattr(userResult, key, value)
