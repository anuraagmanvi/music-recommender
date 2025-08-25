from fastapi import APIRouter

from Logger.Logger import Logger

user_routes = APIRouter()

logger = Logger("UserRoutes").get_logger()


@user_routes.get("/")
def user_home():
    logger.info(f"User home route called")
    return "Welcome USER"


@user_routes.get("/login")
def login():
    pass