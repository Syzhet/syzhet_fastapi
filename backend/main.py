from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .config import base_config
from .api.routers import router

app = FastAPI()

app.include_router(
    router=router,
    prefix='/api/v1'
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

if __name__ == '__main__':
    uvicorn.run(
        app, host=base_config.app.app_host,
        port=base_config.app.app_port
    )
