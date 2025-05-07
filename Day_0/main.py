from models.user import User
from services.user_service import UserService

def main() -> None:
    """Entry point for the User Management application."""
    service = UserService()
    service.add_user(User(id=1, name="Ankita", email="ankitasinha2912@gmail.com"))
    service.add_user(User(id=2, name="Shreya", email="Shreya@gmail.com"))

    try:
        user = service.get_user_by_id(1)
        print(f"Found user: {user.name} - {user.email}")
    except Exception as e:
        print(str(e))

    print("All users:")
    for user in service.list_users():
        print(f"{user.name} ({user.email})")

if __name__ == "__main__":
    main()
