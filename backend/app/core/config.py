from pydantic_settings import BaseSettings, SettingsConfigDict
#DATABASE_URL — the connection string to Mongo or Postgres
#JWT_SECRET — a random secret string used to sign login tokens
#JWT_ALGORITHM — which algorithm to sign tokens 
#ACCESS_TOKEN_EXPIRE_MINUTES — how long a login token stays valid
#ENVIRONMENT — a label like development or production

class Setting(BaseSettings):
    DataBase_url : str
    JWT_Secret : str
    JWT_Algorithm: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int= 60
    Environment: str = "development"
    model_config = SettingsConfigDict(env_file=".env")
settings = Setting()

if __name__ == "__main__":
    print(settings.JWT_Secret)


