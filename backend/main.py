import uvicorn
from fastapi import FastAPI

from .api.routers import router
from .config import base_config

app: FastAPI = FastAPI()

app.include_router(
    router=router,
    prefix='/api/v1'
)

if __name__ == '__main__':
    uvicorn.run(
        app, host=base_config.app.app_host,
        port=base_config.app.app_port
    )
