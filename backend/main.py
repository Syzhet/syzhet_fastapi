from fastapi import FastAPI
import uvicorn

from .config import base_config
from .api.routers import router

app = FastAPI()

app.include_router(
    router=router,
    prefix='/api/v1'
)

if __name__ == '__main__':
    uvicorn.run(
        app, host=base_config.app.app_host,
        port=base_config.app.app_port
    )
