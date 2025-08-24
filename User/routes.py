from fastapi import APIRouter

user_routes = APIRouter()


@user_routes.get("/")
def user_home():
    return "Welcome USER"