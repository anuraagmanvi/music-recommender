# Created by Anuraag on 15-08-25
import os

os.environ["PYTHONPATH"] = os.getcwd()

import uvicorn
from fastapi import FastAPI

from Logger.Logger import Logger
from User.routes import user_routes

app = FastAPI()

app.include_router(user_routes, prefix="/user", tags=["users"])

logger = Logger("run").get_logger()



if __name__ == "__main__":
    logger.info("Server is now running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
