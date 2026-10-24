from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME : str = "holi_app"
    PROJECT_VERSION : str = "0.0.1"
    DATABASE_URL : str

    SECRET_KEY: str # para el token
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: 60

    class Config:
        env_file = '.env'
        extra = "ignore" # muy importante 


settings = Settings()