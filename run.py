# Created by Anuraag on 15-08-25

import uvicorn
from fastapi import FastAPI

from User.routes import user_routes

app = FastAPI()

app.include_router(user_routes, prefix="/user", tags=["users"])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
