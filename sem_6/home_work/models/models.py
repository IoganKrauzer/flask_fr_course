from pydantic import BaseModel, Field, EmailStr
import datetime
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ProductIn(BaseModel):
    title: str
    description: str
    price: float


class Product(ProductIn):
    id: int


class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    def get_password_hash(self):
        self.password = pwd_context.hash(self.password)


class User(UserIn):
    id: int


class OrderIn(BaseModel):
    user_id: int = Field(..., title="User ID")
    product_id: int = Field(..., title="Product ID")
    date: datetime.date = Field(..., title="Created at")
    status: str = Field(..., title="Status")


class Order(OrderIn):
    order_id: int
