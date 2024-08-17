import datetime
from random import randint, choice
from fastapi import APIRouter
from sem_6.home_work.db import users, orders, products, database

router = APIRouter()


@router.get("/fake_data/{count}")
async def create_fake_users(fake_data_count: int):
    for i in range(fake_data_count):

        query = users.insert().values(
            first_name=f"Name_{i + 1}",
            last_name=f"LastName_{i + 1}",
            email=f"user{i + 1}@mail.ru",
            password=f"pass{randint(10, 20)}",
        )
        await database.execute(query)

    for j in range(fake_data_count * 2):
        query = products.insert().values(
            title=f"Item_{j + 1}",
            description=f"Description_{j + 1}",
            price=randint(1000, 10000) / 100,
        )
        await database.execute(query)

    for k in range(fake_data_count):
        query = orders.insert().values(
            user_id=randint(1, fake_data_count + 1),
            product_id=randint(1, fake_data_count + 1),
            date=datetime.datetime.now(),
            status=choice(["Done", "In work", "Canceled"]),
        )
        await database.execute(query)

    return {
        "message": f"{fake_data_count} users, {fake_data_count * 2} products and {fake_data_count} orders were created"
    }
