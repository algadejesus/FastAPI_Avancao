from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int
    email: str
    
    @validator('email')
    def validate_email(cls,value):
        if '@' not in value:
            raise ValueError('Invalid email')
        return value
    
    @validator('age')
    def validate_age(cls,value):
        if value <= 0 not in value:
            raise ValueError('Invalid email')
        return value

def UserFunction(user: User):
    return f"Name: {user.name}, Age: {user.age}, Email: {user.email}"

# Criação do objeto User
user = User(name='Alexandre de Jesus', age=6 ,email='agladejesus@gmail.br')

# Passando o objeto User para a função
txUser = UserFunction(user)

print(txUser)
