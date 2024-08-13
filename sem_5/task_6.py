import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
users = []

templates = Jinja2Templates(directory="templates")


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class User(UserIn):
    id: int


for i in range(10):
    users.append(
        User(
            id=i + 1,
            name=f"Name_{i + 1}",
            email=f"Email{i + 1}@mail.ru",
            password="123",
        )
    )


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


if __name__ == "__main__":
    uvicorn.run("task_6:app", host="127.0.0.1", port=8000, reload=True)
