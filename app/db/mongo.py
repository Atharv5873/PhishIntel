from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # This loads .env file

MONGODB_URI = os.getenv("MONGO_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables!")

client = AsyncIOMotorClient(MONGODB_URI)
db = client["phishintel"]
detections = db["detections"]
