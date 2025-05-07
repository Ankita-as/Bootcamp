from pydantic import BaseModel, conint, constr, field_validator, ValidationError
from typing import Optional

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)
    profile: Optional[Profile] = None
    email: Optional[str] = None
    
    # Correct way to use field_validator in Pydantic V2
    @field_validator('name')
    def check_name_capitalization(cls, v):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v

try:
    # Valid user input
    user_data = {"name": "Alice", "age": 30}
    user = User(**user_data)
    print(user.model_dump())
    print(user.model_dump_json())
except ValidationError as e:
    print(e)

try:
    # Example with invalid name capitalization
    invalid_user = User(name="bob", age=25)
except ValidationError as e:
    print(e)

try:
    # Correct input
    user_data = {"name": "Alice", "age": 42}
    user = User(**user_data)
    print(user.model_dump())
    print(user.model_dump_json())
    
    # Nested model
    user_data_with_profile = {
        "name": "Alice", 
        "age": 30, 
        "profile": {"bio": "Web Developer", "website": "https://alice.dev"}
    }
    user_with_profile = User(**user_data_with_profile)
    print(user_with_profile.model_dump())
except ValidationError as e:
    print(e)