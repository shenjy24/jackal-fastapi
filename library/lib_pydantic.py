from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


# 创建模型的实例
data = {
    "name": "Alice",
    "age": 30
}

person = Person(**data)

# 访问属性
print(person.name)  # 输出：Alice
print(person.age)  # 输出：30
