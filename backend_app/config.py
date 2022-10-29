from pydantic import BaseModel, BaseSettings


class AppConfig(BaseModel):
    app_host: str
    app_port: str


class DbConfig(BaseModel):
    db_host: str
    database: str
    db_user: str
    db_password: str
    db_port: str


class BaseConfig(BaseSettings):
    app: AppConfig
    db: DbConfig

    class Config:
        env_nested_delimiter = '__'


base_config = BaseConfig(_env_file='infra/.env', _env_file_encoding='utf-8')
