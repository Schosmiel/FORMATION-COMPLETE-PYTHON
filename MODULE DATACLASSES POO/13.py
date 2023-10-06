from dataclasses import dataclass

@dataclass
class User:
    first_name : str
    last_name : str

user_01=User(first_name="Patric", last_name="Smith")


print(user_01.first_name)

print(user_01.last_name)