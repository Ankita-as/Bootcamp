from dataclasses import dataclass, field
from collections import namedtuple

# 1. Basic Dataclass
@dataclass
class User:
    name: str
    age: int = 0  # 2. Default value

    # 5. Custom method in dataclass
    def is_adult(self) -> bool:
        return self.age >= 18

# 3. Frozen Dataclass
@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int

# 8. Inheritance in Dataclass
@dataclass
class AdminUser(User):
    access_level: int = 1

# 6. NamedTuple Basics
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)

# 7. Field Rename
InvalidPoint = namedtuple('InvalidPoint', ['x', 'class'], rename=True)

# Main test section
if __name__ == "__main__":
    # Basic User
    u1 = User("Alice", 20)
    u2 = User("Bob")
    print(u1)
    print(u2)

    # 4. Comparison Support
    u3 = User("Alice", 20)
    print("u1 == u3:", u1 == u3)

    # Custom Method
    print("Is Alice adult?", u1.is_adult())
    print("Is Bob adult?", u2.is_adult())

    # Frozen Dataclass
    fuser = FrozenUser("Charlie", 25)
    print(fuser)
    # fuser.age = 30  # Uncommenting this will raise FrozenInstanceError

    # NamedTuple
    print("Point:", p1)
    print("x coordinate:", p1.x)

    # Field Rename in NamedTuple
    ip = InvalidPoint(10, 20)
    print("InvalidPoint with renamed fields:", ip)

    # Inheritance
    admin = AdminUser("Admin", 35, access_level=5)
    print("Admin:", admin)
