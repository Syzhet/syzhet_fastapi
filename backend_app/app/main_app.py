from fastapi import FastAPI
import uvicorn

from backend_app.config import base_config

app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(
        app, host=base_config.app.app_host,
        port=base_config.app.app_port
    )
