import os
from dotenv import load_dotenv
load_dotenv()       # Load environment variables from .env


# Format: SETTING = os.getenv(key, default value)
class Config:
    # Get "SECRET_KEY" from .env (for sessions and security)
    # "default-secret" to prevent app from crashing if SECRET_KEY doesn't exist in .env
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    
    # Get "DATABASE_URL" from .env (how SQLAlchemy connects to the database)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Tells FLask-SQLAlchemy whether or not to track object changes (Setting to True adds more overhead and uses more memory)
    # Not needed - Set to False to avoid performance issues
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Get the DEBUG setting from .env as a string ("True" or "False")
    # Compare that string to "True" (== True) and set the value to DEBUG
    DEBUG = os.getenv("DEBUG", "False") == "True"





