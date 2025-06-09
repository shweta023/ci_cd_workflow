import dotenv
import os
dotenv.load_dotenv()
print("Environment variables loaded from .env file.")
print(f"DB Name:{os.getenv('db_name')}")