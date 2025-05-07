from dataclasses import dataclass, field
from typing import List

# 1. Basic Dataclass
@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

    def is_adult(self):
        return self.age >= 18


# 2. Frozen Dataclass
@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int


# 3. Comparison Support
user1 = User(name="Alice", age=25, tags=["admin"])
user2 = User(name="Alice", age=25, tags=["admin"])

print("User1 == User2:", user1 == user2)  # Should be True

# 4. is_adult Method
print("Is User1 an adult?", user1.is_adult())  # Should be True

# 5. Default Country
print("User1 country:", user1.country)  # Should print "India"

# 6. Factory Default for tags
print("User1 tags:", user1.tags)  # Should be ["admin"]

# 7. Post-Init Validation (Uncomment to see it raise an error)
# invalid_user = User(name="Bob", age=-5)

# 8. Frozen Dataclass Example
frozen_user = FrozenUser(name="Charlie", age=30)
print("Frozen user:", frozen_user)

# Attempt to modify a frozen dataclass (should raise error)
# frozen_user.age = 35  # Uncommenting this will raise: dataclasses.FrozenInstanceError

# 9. Slots Dataclass
@dataclass(slots=True)
class SlimUser:
    name: str
    age: int

slim_user = SlimUser(name="Daisy", age=22)
print("Slim user:", slim_user)
