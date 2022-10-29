from backend_app import config

from fastapi import FastAPI
import uvicorn




app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(
        app, host=base_config.app.app_host,
        port=base_config.app.app_port
    )
