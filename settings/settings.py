from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str


settings = Settings()