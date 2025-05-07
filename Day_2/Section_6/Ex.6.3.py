from pydantic import BaseModel, conint, constr, Field, ValidationError
from typing import Optional

class Profile(BaseModel):
    """
    A profile of a user with personal details.
    """
    bio: str = Field(..., description="A brief bio of the user")
    website: str = Field(..., description="The user's personal or professional website URL")

class User(BaseModel):
    """
    User model representing a user of the system with personal and contact information.
    """
    id: conint(gt=0) = Field(..., alias="user_id", description="Unique identifier for the user")
    name: constr(min_length=3) = Field(..., description="Full name of the user (at least 3 characters)")
    age: conint(gt=0) = Field(..., description="Age of the user (must be greater than 0)")
    email: Optional[str] = Field(None, description="Email address of the user")
    profile: Optional[Profile] = Field(None, description="The user's profile information")

    class Config:
        # Ensure that the alias works when parsing input
        validate_by_name = True

# Example usage:

# Valid user input with JSON field "user_id" mapped to field "id"
user_data = {
    "user_id": 1,
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "profile": {
        "bio": "Web Developer",
        "website": "https://alice.dev"
    }
}

try:
    user = User(**user_data)
    # Using `model_dump` for serializing the model
    print(user.model_dump())
    # Using `model_dump_json` for JSON serialization
    print(user.model_dump_json())
except ValidationError as e:
    print(e)
