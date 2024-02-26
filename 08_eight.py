import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

# Connection to MongoDB
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client["learning"]
movies = db["videos"]


def add_video():
    title = input("Enter the title of the video: ")
    url = input("Enter the url of the video: ")
    duration = input("Enter the duration of the video: ")
    movies.insert_one({
        "title": title,
        "url": url,
        "duration": duration
    })
    print("Video added successfully")


def delete_video():
    title = input("Enter the title of the video to delete: ")
    result = movies.delete_one({"title":
                                title})
    if result.deleted_count:
        print("Video deleted successfully")
    else:
        print("Video not found")

def edit_video():
    title = input("Enter the title of the video to edit: ")
    result = movies.find_one({"title": title})
    if result:
        new_title = input("Enter the new title of the video: ")
        new_url = input("Enter the new url of the video: ")
        new_duration = input("Enter the new duration of the video: ")
        movies.update_one({"title": title}, {
            "$set": {
                "title": new_title,
                "url": new_url,
                "duration": new_duration
            }
        })
        print("Video edited successfully")
    else:
        print("Video not found")


def list_of_videos():
    for video in movies.find():
        print(f"Title: {video['title']}, URL: {video['url']}, Duration: {video['duration']}")
    if not movies.count_documents({}):
        print("No videos found")


def main():
    print("Welcome to the Video Manager")
    print("1. Add a video")
    print("2. Delete a video")
    print("3. Edit a video")
    print("4. View all videos")
    print("5. Exit")

    choice = (input("Enter your choice: "))
    if choice == "1":
        add_video()
    elif choice == "2":
        delete_video()
    elif choice == "3":
        edit_video()
    elif choice == "4":
        list_of_videos()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

