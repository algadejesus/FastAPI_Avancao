from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

def f(user: User):
    user.name

user = User(name='Alexandre de Jesus', age=39, email='agladejesus@gmail.com')

print(user)