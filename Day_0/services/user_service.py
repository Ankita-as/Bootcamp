from typing import List, Optional
from models.user import User
from utils.exceptions import UserNotFoundError

class UserService:
    def __init__(self) -> None:
        self._users: List[User] = []

    def add_user(self, user: User) -> None:
        """Add a new user to the list."""
        self._users.append(user)

    def get_user_by_id(self, user_id: int) -> User:
        """Fetch a user by their ID."""
        for user in self._users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(f"User with id {user_id} not found.")

    def list_users(self) -> List[User]:
        """Return all users."""
        return self._users
