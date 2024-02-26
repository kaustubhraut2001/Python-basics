import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

# Connection to MongoDB
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client["learning"]
movies = db["videos"]





def main():
    print("Welcome to the Video Manager")
    print("1. Add a video")
    print("2. Delete a video")
    print("3. Edit a video")
    print("4. View all videos")
    print("5. Exit")

  

if __name__ == "__main__":
    main()

