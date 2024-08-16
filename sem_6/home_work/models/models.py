from pydantic import BaseModel, Field, EmailStr
import datetime


class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float


class ProductIn(BaseModel):
    title: str
    description: str
    price: float


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Order(BaseModel):
    order_id: int
    user_id: int
    product_id: int
    order_date: datetime.date
    order_status: str


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: datetime.date
    status: str
